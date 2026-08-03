"""
Optimizer Factory
"""

import torch.optim as optim

from backend.config.segformer_config import (
    LEARNING_RATE,
    WEIGHT_DECAY,
)


def get_optimizer(model):

    return optim.AdamW(
        model.parameters(),
        lr=LEARNING_RATE,
        weight_decay=WEIGHT_DECAY,
    )