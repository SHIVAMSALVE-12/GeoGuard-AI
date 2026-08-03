import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from backend.config.dataset_config import (
    DATASET_ROOT,
    TRAIN_TXT,
)

from backend.datasets.loaders.openearthmap_dataset import (
    OpenEarthMapDataset,
)

from backend.datasets.transforms.transforms import (
    get_train_transforms,
)

from backend.visualization.visualize_dataset import (
    visualize_sample,
)


def main():

    dataset = OpenEarthMapDataset(
        dataset_root=DATASET_ROOT,
        split_file=TRAIN_TXT,
        transform=get_train_transforms(),
    )

    sample = dataset[0]

    visualize_sample(sample)


if __name__ == "__main__":
    main()