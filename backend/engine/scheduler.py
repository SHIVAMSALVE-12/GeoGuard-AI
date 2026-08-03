"""
Learning Rate Scheduler
"""

from torch.optim.lr_scheduler import CosineAnnealingLR

from backend.config.segformer_config import NUM_EPOCHS


def get_scheduler(optimizer):

    return CosineAnnealingLR(
        optimizer,
        T_max=NUM_EPOCHS,
    )