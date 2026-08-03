"""
GeoGuard AI

Land Cover Training Entry Point

Author: Shivam Salve
"""

from backend.training.factory import (
    TrainingFactory,
)

from backend.training.pipeline import (
    TrainingPipeline,
)

from backend.training.configs.landcover import (
    landcover_config,
)


def main():

    components = TrainingFactory.create(
        "landcover"
    )

    pipeline = TrainingPipeline(
        config=landcover_config,
        components=components,
    )

    pipeline.fit()


if __name__ == "__main__":
    main()