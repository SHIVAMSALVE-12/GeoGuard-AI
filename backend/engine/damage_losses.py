"""
GeoGuard AI

Damage Loss Functions

Author: Shivam Salve
"""

import torch.nn as nn


class DamageLoss(nn.Module):
    """
    Multi-class loss for building damage segmentation.
    """

    def __init__(
        self,
        ignore_index=-1,
    ):

        super().__init__()

        self.loss = nn.CrossEntropyLoss(
            ignore_index=ignore_index,
        )

    def forward(
        self,
        logits,
        labels,
    ):

        return self.loss(
            logits,
            labels,
        )


def get_damage_loss():

    return DamageLoss()