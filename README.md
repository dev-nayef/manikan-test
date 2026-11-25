# ACGPN — Virtual Try-On

This repository now points to the upstream ACGPN implementation as a Git submodule.

## Get the source

```bash
git clone --recurse-submodules https://github.com/dev-nayef/manikan-test.git
cd manikan-test/ACGPN
```

If you already cloned without submodules:

```bash
git submodule update --init --recursive
```

Read the upstream [ACGPN README](https://github.com/minar09/ACGPN) for dataset preparation, checkpoints, dependencies, and inference instructions.

## Important

- This is a Python/PyTorch research project, not a static HTML site. GitHub Pages cannot run the model.
- The upstream repository states that use is restricted to non-commercial research and educational purposes. Obtain permission before any commercial use.
- Pretrained checkpoints and datasets must be downloaded separately from the links provided upstream.
- This repository preserves the upstream project through a submodule; it does not copy or relicense its code.
