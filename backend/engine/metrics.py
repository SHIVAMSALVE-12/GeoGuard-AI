"""
GeoGuard AI

Generic Segmentation Metrics

Author: Shivam Salve
"""

import torch
import torch.nn.functional as F

from torchmetrics.classification import (
    MulticlassJaccardIndex,
)


class SegmentationMetrics:
    """
    Generic metrics for semantic segmentation.

    Supports:
    - Land Cover
    - Flood
    - Damage Assessment
    """

    def __init__(
        self,
        num_classes: int,
        device,
        ignore_index: int | None = None,
    ):

        self.device = device

        self.ignore_index = ignore_index

        kwargs = dict(
            num_classes=num_classes,
            average="macro",
        )

        if ignore_index is not None:
            kwargs["ignore_index"] = ignore_index

        self.miou = MulticlassJaccardIndex(
            **kwargs
        ).to(device)

    def _resize_logits(
        self,
        logits,
        labels,
    ):

        if logits.shape[-2:] != labels.shape[-2:]:

            logits = F.interpolate(
                logits,
                size=labels.shape[-2:],
                mode="bilinear",
                align_corners=False,
            )

        return logits

    def pixel_accuracy(
        self,
        logits,
        labels,
    ):

        logits = self._resize_logits(
            logits,
            labels,
        )

        preds = torch.argmax(
            logits,
            dim=1,
        )

        if self.ignore_index is not None:

            valid = labels != self.ignore_index

            preds = preds[valid]

            labels = labels[valid]

        correct = (preds == labels).float().sum()

        total = labels.numel()

        if total == 0:
            return 0.0

        return (correct / total).item()

    def mean_iou(
        self,
        logits,
        labels,
    ):

        logits = self._resize_logits(
            logits,
            labels,
        )

        preds = torch.argmax(
            logits,
            dim=1,
        )

        return self.miou(
            preds,
            labels,
        ).item()

    def dice_score(
        self,
        logits,
        labels,
    ):

        logits = self._resize_logits(
            logits,
            labels,
        )

        preds = torch.argmax(
            logits,
            dim=1,
        )

        if self.ignore_index is not None:

            valid = labels != self.ignore_index

            preds = preds[valid]

            labels = labels[valid]

        intersection = (
            preds == labels
        ).float().sum()

        total = (
            preds.numel()
            + labels.numel()
        )

        if total == 0:
            return 0.0

        dice = (
            2.0 * intersection
        ) / total

        return dice.item()