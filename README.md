# ACGPN — Local Virtual Try-On Lab

واجهة HTML محلية لتشغيل كود ACGPN الأصلي وعرض نتيجة inference. تم الاحتفاظ بـ ACGPN كمستودع فرعي (submodule)، وأضيف خادم FastAPI بسيط لربط الصفحة بـ Python.

## تشغيل الواجهة على Windows

1. ثبّت Python 3.8 أو إصداراً متوافقاً مع إصدارات PyTorch التي يتطلبها المشروع.
2. نزّل المستودع مع الـ submodule:

   ```bash
   git clone --recurse-submodules https://github.com/dev-nayef/manikan-test.git
   cd manikan-test
   ```

3. نزّل **Dataset_Test** و**Checkpoints** من الروابط الموجودة في [README الأصلي](https://github.com/minar09/ACGPN)، ثم جهّز المجلدات كما يتوقع الكود:
   - بيانات الاختبار داخل `ACGPN/Data_preprocessing/`
   - أوزان النموذج داخل `ACGPN/checkpoints/label2city/`
4. ثبّت متطلبات ACGPN الأصلية ومتطلبات واجهة الويب:

   ```bash
   python -m pip install -r ACGPN/requirements.txt
   python -m pip install -r requirements-local.txt
   ```

   ثبّت نسخة PyTorch المناسبة لجهازك من تعليمات PyTorch الرسمية. المشروع الأصلي يستدعي CUDA افتراضياً؛ التشغيل على CPU قد يتطلب تعديلات على إعدادات GPU.
5. شغّل `run.bat` وافتح [http://127.0.0.1:8000](http://127.0.0.1:8000).

زر **فحص التجهيزات** يتحقق من وجود مجلد البيانات والأوزان. زر **تشغيل تجربة ACGPN الفعلية** يشغّل `ACGPN/test.py` بإعداداته الأصلية ثم يعرض أحدث صورة ناتجة.

## حدود النسخة

- هذه واجهة محلية فوق اختبار ACGPN الأصلي، وليست خدمة رفع صور شخصية وتجربة فورية. تشغيل صورة جديدة يتطلب pipeline تجهيز الشخص (human parsing وpose/agnostic generation) المتوافق مع ACGPN، وهو غير مضمن في هذا المستودع.
- نموذج VITON الأصلي مدرّب أساساً على صور أمامية لنساء وقطع ملابس علوية؛ لا تعتبره تجربة جاهزة للبنطال والحذاء.
- مستودع ACGPN الأصلي يقيّد الاستخدام بالبحث والتعليم غير التجاري. راجع الترخيص قبل أي استخدام آخر.
- لا ترفع الخادم على الإنترنت؛ هو مصمم للاستخدام المحلي على جهازك فقط.

## المصدر

[ACGPN by minar09](https://github.com/minar09/ACGPN) · [Paper (CVPR 2020)](https://arxiv.org/abs/2003.05863)
