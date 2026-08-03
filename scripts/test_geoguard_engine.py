"""
GeoGuard AI

Test GeoGuard Engine

Author: Shivam Salve
"""

from pathlib import Path

from backend.geoguard.engine import (
    GeoGuardEngine,
)


def main():

    engine = GeoGuardEngine()

    # --------------------------------------------------
    # Test Images
    # --------------------------------------------------

    landcover_image = None
    flood_image = None

    damage_image = Path(
        "backend/datasets/test_damage.png"
    )

    # --------------------------------------------------
    # Run GeoGuard AI
    # --------------------------------------------------

    result = engine.predict(

        landcover_image=landcover_image,

        flood_image=flood_image,

        damage_image=damage_image,

    )

    print("=" * 70)

    print(result)

    print("=" * 70)


if __name__ == "__main__":

    main()