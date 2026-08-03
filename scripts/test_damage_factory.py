from backend.training.factory import (
    TrainingFactory,
)

components = TrainingFactory.create(
    "damage"
)

print("=" * 70)

print(type(components.model))

print(len(components.train_loader))

print(len(components.val_loader))

print(type(components.loss_fn))

print(type(components.metrics))

print("=" * 70)