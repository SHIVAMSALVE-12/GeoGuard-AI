"""
GeoGuard AI

Recommendation Engine

Author: Shivam Salve
"""

from backend.intelligence.schemas import (
    FloodResult,
    DamageResult,
    ChangeDetectionResult,
)


class RecommendationEngine:
    """
    Generates disaster response recommendations
    based on AI model outputs.
    """

    def __init__(self):
        pass

    def generate(
        self,
        flood: FloodResult | None = None,
        damage: DamageResult | None = None,
        change: ChangeDetectionResult | None = None,
    ):

        recommendations = []

        # ---------------------------------------
        # Flood
        # ---------------------------------------

        if flood is not None:

            if flood.flood_detected:

                recommendations.extend([
                    "Inspect flood-prone regions.",
                    "Monitor water level changes.",
                    "Prepare evacuation plans if required.",
                ])

        # ---------------------------------------
        # Building Damage
        # ---------------------------------------

        if damage is not None:

            if damage.buildings_damaged > 0:

                recommendations.extend([
                    "Assess structural safety.",
                    "Deploy emergency response teams.",
                    "Restrict access to unsafe buildings.",
                ])

        # ---------------------------------------
        # Change Detection
        # ---------------------------------------

        if change is not None:

            if change.change_detected:

                recommendations.extend([
                    "Compare with previous satellite imagery.",
                    "Schedule field inspection.",
                    "Verify detected infrastructure changes.",
                ])

        # ---------------------------------------
        # Default
        # ---------------------------------------

        if len(recommendations) == 0:

            recommendations.append(
                "Continue routine satellite monitoring."
            )

        return recommendations