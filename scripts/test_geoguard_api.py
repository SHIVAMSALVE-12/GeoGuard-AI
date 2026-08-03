"""
GeoGuard AI

End-to-End AI Test

Author: Shivam Salve
"""

from pathlib import Path

from backend.geoguard.engine import (
    GeoGuardEngine,
)


def main():

    engine = GeoGuardEngine()

    result = engine.predict(

        damage_image=Path(
            "backend/datasets/test_damage.png"
        )

    )

    print("\n" + "=" * 70)
    print("ASSESSMENT")
    print("=" * 70)

    print(result.assessment)

    print("\n" + "=" * 70)
    print("AI REASONING")
    print("=" * 70)

    print("Summary\n")
    print(result.reasoning.summary)

    print("\nPriority :", result.reasoning.priority)

    print("\nRecommendations")

    for i, rec in enumerate(
        result.reasoning.recommendations,
        start=1,
    ):
        print(f"{i}. {rec}")

    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()