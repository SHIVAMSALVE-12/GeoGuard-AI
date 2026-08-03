import torch

print("=" * 50)
print("PyTorch GPU Check")
print("=" * 50)

print(f"PyTorch Version : {torch.__version__}")
print(f"CUDA Available  : {torch.cuda.is_available()}")

if torch.cuda.is_available():
    print(f"GPU Name        : {torch.cuda.get_device_name(0)}")
    print(f"CUDA Version    : {torch.version.cuda}")
    print(f"GPU Count       : {torch.cuda.device_count()}")
else:
    print("No CUDA GPU detected.")

print("=" * 50)