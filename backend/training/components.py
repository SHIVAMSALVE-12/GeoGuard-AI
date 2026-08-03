"""
GeoGuard AI

Training Components Container

Author: Shivam Salve
"""

from dataclasses import dataclass


@dataclass
class TrainingComponents:

    model: object

    train_loader: object

    val_loader: object

    optimizer: object

    scheduler: object

    loss_fn: object

    metrics: object

    checkpoint: object

    logger: object