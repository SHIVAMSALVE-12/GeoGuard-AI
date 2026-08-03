from pathlib import Path

from backend.inference.damage_preprocess import (
    DamagePreprocessor,
)

IMAGE = Path(
    "backend/datasets/test_damage.png"
)

processor = DamagePreprocessor()

image, tensor = processor.preprocess_file(
    IMAGE
)

print("=" * 60)

print(image.shape)

print(tensor.shape)

print(tensor.dtype)

print("=" * 60)