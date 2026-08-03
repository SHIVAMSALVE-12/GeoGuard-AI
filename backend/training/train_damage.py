"""
GeoGuard AI

Damage Training

Author: Shivam Salve
"""

from backend.training.factory import (
    TrainingFactory,
)

from backend.training.pipeline import (
    TrainingPipeline,
)

from backend.training.configs.damage import (
    damage_config,
)


def main():

    components = TrainingFactory.create(
        task="damage",
    )

    pipeline = TrainingPipeline(
        config=damage_config,
        components=components,
    )

    pipeline.fit()


if __name__ == "__main__":

    main()