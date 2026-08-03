import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.insert(0, str(PROJECT_ROOT))

import torch

from backend.models.flood_segformer import (
    build_flood_segformer,
)

model = build_flood_segformer()

print("=" * 70)

print("Model Loaded Successfully")

dummy = torch.randn(
    1,
    2,
    512,
    512,
)

with torch.no_grad():

    output = model(
        pixel_values=dummy,
    )

print()

print("Output Shape :", output.logits.shape)

print()

print("Classes :", output.logits.shape[1])

print("=" * 70)