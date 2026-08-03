"""
Loss Functions for GeoGuard AI
"""

import torch.nn as nn

from backend.config.dataset_config import IGNORE_LABEL


def get_loss_function():

    """
    Cross Entropy Loss for Semantic Segmentation
    """

    return nn.CrossEntropyLoss(
        ignore_index=IGNORE_LABEL
    )