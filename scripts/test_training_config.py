import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.insert(0, str(PROJECT_ROOT))

from backend.training.configs import TrainingConfig

import torch

cfg = TrainingConfig(

    name="Flood",

    num_epochs=40,

    batch_size=4,

    learning_rate=6e-5,

    weight_decay=1e-4,

    image_size=512,

    num_workers=0,

    pin_memory=True,

    num_classes=2,

    in_channels=2,

    device=torch.device("cuda"),

    use_amp=True,

    checkpoint_dir=Path("checkpoints"),

    log_dir=Path("logs"),

    seed=42,

    ignore_index=-1,

)

print("=" * 70)

print(cfg)

print("=" * 70)