import sys
from pathlib import Path

import torch

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from backend.engine.metrics import SegmentationMetrics

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

metrics = SegmentationMetrics(device)

preds = torch.randn(2, 9, 512, 512).to(device)

labels = torch.randint(
    0,
    9,
    (2, 512, 512)
).to(device)

print("=" * 60)

print("Pixel Accuracy :", metrics.pixel_accuracy(preds, labels))

print("Mean IoU       :", metrics.mean_iou(preds, labels))

print("Dice Score     :", metrics.dice_score(preds, labels))

print("=" * 60)