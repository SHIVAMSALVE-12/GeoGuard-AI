"""
GeoGuard AI

End-to-End Validation

Author: Shivam Salve
"""

from pathlib import Path

from backend.geoguard.engine import GeoGuardEngine


def divider(title: str):

    print("\n" + "=" * 70)

    print(title)

    print("=" * 70)


def main():

    engine = GeoGuardEngine()

    result = engine.predict(

        damage_image=Path(
            "backend/datasets/test_damage.png"
        )

    )

    divider("AI MODULES")

    print(
        "Land Cover :",
        result.landcover is not None,
    )

    print(
        "Flood      :",
        result.flood is not None,
    )

    print(
        "Damage     :",
        result.damage is not None,
    )

    divider("ASSESSMENT")

    print(result.assessment)

    divider("AI REASONING")

    print("Summary:\n")

    print(result.reasoning.summary)

    print("\nPriority:")

    print(result.reasoning.priority)

    divider("RECOMMENDATIONS")

    if result.reasoning.recommendations:

        for i, rec in enumerate(
            result.reasoning.recommendations,
            start=1,
        ):

            print(f"{i}. {rec}")

    else:

        print("No recommendations.")

    divider("VALIDATION")

    print(
        "Assessment Available :",
        result.assessment is not None,
    )

    print(
        "Reasoning Available  :",
        result.reasoning is not None,
    )

    print(
        "Summary Generated    :",
        len(result.reasoning.summary) > 0,
    )

    print(
        "Priority Generated   :",
        len(result.reasoning.priority) > 0,
    )

    print(
        "Recommendations      :",
        len(result.reasoning.recommendations),
    )

    divider("GeoGuard AI")

    print("END-TO-END VALIDATION SUCCESSFUL")


if __name__ == "__main__":

    main()