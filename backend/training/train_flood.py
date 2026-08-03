"""
GeoGuard AI

Flood Training Entry Point

Author: Shivam Salve
"""

from backend.training.factory import (
    TrainingFactory,
)

from backend.training.pipeline import (
    TrainingPipeline,
)

from backend.training.configs.flood import (
    flood_config,
)


def main():

    components = TrainingFactory.create(
        "flood"
    )

    pipeline = TrainingPipeline(
        config=flood_config,
        components=components,
    )

    pipeline.fit()


if __name__ == "__main__":
    main()