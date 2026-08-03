"""
GeoGuard AI

Flood Loss Functions

Author: Shivam Salve
"""

import torch
import torch.nn as nn
import torch.nn.functional as F


class DiceLoss(nn.Module):
    """
    Dice Loss for binary segmentation.
    """

    def __init__(self, smooth=1.0):
        super().__init__()
        self.smooth = smooth

    def forward(self, logits, targets):

        # logits
        probs = torch.softmax(logits, dim=1)

        flood_probs = probs[:, 1]

        valid_mask = targets != -1

        flood_probs = flood_probs[valid_mask]

        targets = targets[valid_mask].float()

        intersection = (flood_probs * targets).sum()

        union = flood_probs.sum() + targets.sum()

        dice = (
            2.0 * intersection + self.smooth
        ) / (
            union + self.smooth
        )

        return 1.0 - dice


class FloodLoss(nn.Module):

    def __init__(self):

        super().__init__()

        self.ce = nn.CrossEntropyLoss(
            ignore_index=-1
        )

        self.dice = DiceLoss()

    def forward(
        self,
        logits,
        labels,
    ):

        ce_loss = self.ce(
            logits,
            labels,
        )

        dice_loss = self.dice(
            logits,
            labels,
        )

        return ce_loss + dice_loss


def get_flood_loss():

    return FloodLoss()