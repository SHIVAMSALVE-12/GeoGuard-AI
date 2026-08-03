import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from backend.models.segformer_model import build_segformer
from backend.engine.losses import get_loss_function
from backend.engine.optimizer import get_optimizer
from backend.engine.scheduler import get_scheduler

model = build_segformer()

loss_fn = get_loss_function()

optimizer = get_optimizer(model)

scheduler = get_scheduler(optimizer)

print("=" * 60)

print("Loss Function :", loss_fn)

print("Optimizer :", optimizer.__class__.__name__)

print("Scheduler :", scheduler.__class__.__name__)

print("=" * 60)