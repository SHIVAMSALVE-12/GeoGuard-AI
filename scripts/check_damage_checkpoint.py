import torch

checkpoint = torch.load(
    "backend/models/damage_checkpoints/best_damage_model.pth",
    map_location="cpu",
)

print("=" * 70)
print("Checkpoint Keys:")
print(checkpoint.keys())
print("=" * 70)

for key, value in checkpoint.items():

    if hasattr(value, "shape"):
        print(f"{key}: {value.shape}")
    else:
        print(f"{key}: {value}")
        