"""
GeoGuard AI

Generic Training Configuration

Author: Shivam Salve
"""

from dataclasses import dataclass
from pathlib import Path

import torch


@dataclass
class TrainingConfig:
    """
    Generic configuration used by any segmentation model.
    """

    # --------------------------------------------------
    # Metadata
    # --------------------------------------------------

    name: str

    # --------------------------------------------------
    # Training
    # --------------------------------------------------

    num_epochs: int

    batch_size: int

    learning_rate: float

    weight_decay: float

    image_size: int

    num_workers: int

    pin_memory: bool

    # --------------------------------------------------
    # Model
    # --------------------------------------------------

    num_classes: int

    in_channels: int

    # --------------------------------------------------
    # Device
    # --------------------------------------------------

    device: torch.device

    use_amp: bool

    # --------------------------------------------------
    # Logging
    # --------------------------------------------------

    checkpoint_dir: Path

    log_dir: Path

    # --------------------------------------------------
    # Random Seed
    # --------------------------------------------------

    seed: int

    # --------------------------------------------------
    # Optional
    # --------------------------------------------------

    ignore_index: int | None = None

    # --------------------------------------------------
    # Checkpoint Files
    # --------------------------------------------------

    best_model_name: str = "best_model.pth"

    last_model_name: str = "last_model.pth"