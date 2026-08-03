import torch

from backend.engine.metrics import (
    SegmentationMetrics,
)

metrics = SegmentationMetrics(
    num_classes=5,
    device=torch.device("cpu"),
)

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

print("=" * 70)

print(
    "Pixel Accuracy:",
    metrics.pixel_accuracy(
        logits,
        labels,
    ),
)

print(
    "Mean IoU:",
    metrics.mean_iou(
        logits,
        labels,
    ),
)

print(
    "Dice:",
    metrics.dice_score(
        logits,
        labels,
    ),
)

print("=" * 70)