from pathlib import Path

from backend.inference.flood_preprocess import (
    preprocess_flood_image,
)

IMAGE = Path(
    r"backend/datasets/Sen1Floods11/data/flood_events/HandLabeled/S1Hand/Ghana_103272_S1Hand.tif"
)

original, tensor = preprocess_flood_image(
    IMAGE
)

print("=" * 70)

print("Original Shape :", original.shape)

print("Tensor Shape   :", tensor.shape)

print("Tensor dtype   :", tensor.dtype)

print("=" * 70)