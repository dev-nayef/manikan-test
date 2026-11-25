from pathlib import Path
import subprocess
import sys
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

ROOT = Path(__file__).resolve().parent
MODEL = ROOT / "ACGPN"
app = FastAPI(title="ACGPN Local Demo")
app.mount("/static", StaticFiles(directory=ROOT), name="static")

@app.get("/")
def home():
    return FileResponse(ROOT / "index.html")

def inspect_setup():
    missing = []
    if not (MODEL / "test.py").exists():
        missing.append("مجلد ACGPN غير موجود أو لم يتم تنزيل الـ submodule.")
    if not (MODEL / "checkpoints").exists():
        missing.append("ملفات checkpoints غير موجودة (نزّلها من رابط المشروع الأصلي).")
    if not (MODEL / "datasets" / "test").exists() and not (MODEL / "test").exists():
        missing.append("بيانات Dataset_Test غير موجودة/لم توضع في بنية المشروع.")
    return missing

@app.get("/api/status")
def status():
    missing = inspect_setup()
    return {"ready": not missing, "message": "فحص ACGPN:\n" + ("\n".join("• " + x for x in missing) if missing else "المجلدات الأساسية موجودة. قد تظهر متطلبات أخرى عند بدء inference.")}

@app.post("/api/run-demo")
def run_demo():
    missing = inspect_setup()
    if missing:
        return {"ok": False, "message": "لا يمكن تشغيل النموذج بعد:\n" + "\n".join("• " + x for x in missing)}
    script = MODEL / "test.py"
    try:
        proc = subprocess.run([sys.executable, str(script)], cwd=MODEL, capture_output=True, text=True, timeout=1800)
    except subprocess.TimeoutExpired:
        return {"ok": False, "message": "انتهت مهلة التشغيل بعد 30 دقيقة. افحص موارد الجهاز وسجلات النموذج."}
    except Exception as exc:
        return {"ok": False, "message": f"تعذر تشغيل النموذج: {exc}"}
    if proc.returncode != 0:
        log = (proc.stderr or proc.stdout or "لا يوجد سجل").strip()
        return {"ok": False, "message": "فشل تشغيل ACGPN. آخر سجل:\n" + log[-3500:]}
    candidates = []
    for folder in (MODEL / "results", MODEL / "results_dir", MODEL):
        if folder.exists():
            candidates.extend(p for p in folder.rglob("*") if p.suffix.lower() in {".png", ".jpg", ".jpeg"} and "try-on" in str(p).lower())
    if not candidates:
        return {"ok": True, "message": "انتهى test.py بنجاح، لكن لم أعثر على صور النتائج. راجع مجلد results_dir داخل ACGPN وسجل الإعدادات."}
    newest = max(candidates, key=lambda p: p.stat().st_mtime)
    return {"ok": True, "message": "اكتمل inference بنجاح. هذه أحدث صورة ناتجة من ACGPN.", "image": "/api/result/" + newest.relative_to(MODEL).as_posix()}

@app.get("/api/result/{relative_path:path}")
def result_image(relative_path: str):
    path = (MODEL / relative_path).resolve()
    if MODEL.resolve() not in path.parents or not path.is_file():
        return {"error": "Result not found"}
    return FileResponse(path)
