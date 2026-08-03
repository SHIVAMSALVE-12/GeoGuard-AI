import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.insert(0, str(PROJECT_ROOT))

from backend.training.factory import (
    TrainingFactory,
)

components = TrainingFactory.create(
    "flood"
)

print("=" * 70)

print(type(components.model))

print(type(components.optimizer))

print(type(components.scheduler))

print(type(components.loss_fn))

print(type(components.train_loader))

print(type(components.val_loader))

print(type(components.metrics))

print(type(components.checkpoint))

print(type(components.logger))

print("=" * 70)