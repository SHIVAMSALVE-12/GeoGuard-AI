import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from backend.models.segformer_model import build_segformer
from backend.engine.optimizer import get_optimizer
from backend.engine.scheduler import get_scheduler
from backend.engine.checkpoint import CheckpointManager
from backend.config.segformer_config import CHECKPOINT_DIR

model = build_segformer()

optimizer = get_optimizer(model)

scheduler = get_scheduler(optimizer)

manager = CheckpointManager(CHECKPOINT_DIR)

manager.save(
    model=model,
    optimizer=optimizer,
    scheduler=scheduler,
    epoch=1,
    best_miou=0.42,
    train_loss=0.91,
    val_loss=0.84,
)

epoch, miou = manager.load(
    model,
    optimizer,
    scheduler,
)

print("=" * 60)
print("Epoch :", epoch)
print("Best mIoU :", miou)
print("=" * 60)