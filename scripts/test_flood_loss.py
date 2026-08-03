import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.insert(0, str(PROJECT_ROOT))

import torch

from backend.engine.flood_losses import (
    get_flood_loss,
)

loss_fn = get_flood_loss()

logits = torch.randn(
    2,
    2,
    512,
    512,
)

labels = torch.randint(
    -1,
    2,
    (
        2,
        512,
        512,
    ),
)

loss = loss_fn(
    logits,
    labels,
)

print("=" * 60)

print(loss)

print("=" * 60)