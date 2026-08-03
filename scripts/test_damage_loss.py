import torch

from backend.engine.damage_losses import (
    get_damage_loss,
)

loss_fn = get_damage_loss()

logits = torch.randn(
    2,
    5,
    512,
    512,
)

labels = torch.randint(
    0,
    5,
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

print("=" * 70)

print(loss)

print("=" * 70)