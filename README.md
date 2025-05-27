## CPU-Only Version (No GPU Required)

- This version is optimized to run on any modern CPU.
- No GPU or CUDA is required. GPU-specific dependencies and logic are removed.
- All computation is forced to CPU.
- Performance will depend on your CPU—more cores = faster.

### Installation

```bash
pip uninstall torch torchaudio  # Remove any GPU/CUDA wheels first!
pip install torch torchaudio    # Installs CPU-only versions by default
pip install -r requirements-uv.txt
```

### Notes

- All device checks are forced to CPU.
- CUDA/FlashAttention/other GPU-specific features are disabled or removed.
- If you encounter issues, open an issue in this repository.