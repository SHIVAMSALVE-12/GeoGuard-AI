"""
GeoGuard AI

Assessment Engine Test

Author: Shivam Salve
"""

from pathlib import Path

from backend.geoguard.engine import GeoGuardEngine
from backend.assessment.engine import AssessmentEngine


def main():

    geo = GeoGuardEngine()

    assessment = AssessmentEngine()

    geo_result = geo.predict(

        damage_image=Path(
            "backend/datasets/test_damage.png"
        )

    )

    result = assessment.build(
        geo_result
    )

    print("=" * 70)

    print(result)

    print("=" * 70)


if __name__ == "__main__":

    main()