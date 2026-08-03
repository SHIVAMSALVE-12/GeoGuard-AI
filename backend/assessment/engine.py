"""
GeoGuard AI

Disaster Assessment Engine

Author: Shivam Salve
"""

from backend.assessment.result import AssessmentResult
from backend.assessment.severity import SeverityCalculator


class AssessmentEngine:
    """
    Builds a unified disaster assessment from
    GeoGuard AI model outputs.
    """

    def build(self, geoguard_result):

        result = AssessmentResult()

        # --------------------------------------------------
        # Damage Statistics
        # --------------------------------------------------

        if geoguard_result.damage is not None:

            stats = geoguard_result.damage.statistics

            result.damage = {
                "No Damage": stats.no_damage_percent,
                "Minor Damage": stats.minor_damage_percent,
                "Major Damage": stats.major_damage_percent,
                "Destroyed": stats.destroyed_percent,
            }

        # --------------------------------------------------
        # Flood Statistics
        # --------------------------------------------------

        if geoguard_result.flood is not None:

            stats = geoguard_result.flood.statistics

            result.flood = {
                "Flooded": stats.flood_percent,
                "Non Flooded": stats.non_flood_percent,
            }

        # --------------------------------------------------
        # Land Cover Statistics
        # --------------------------------------------------
        # Will be integrated after we inspect the
        # land-cover inference output.

        # --------------------------------------------------
        # Calculate Severity
        # --------------------------------------------------

        flooded = result.flood.get("Flooded", 0.0)

        destroyed = result.damage.get("Destroyed", 0.0)

        major = result.damage.get("Major Damage", 0.0)

        severity, impact, confidence = (
            SeverityCalculator.calculate(
                flooded_percent=flooded,
                destroyed_percent=destroyed,
                major_damage_percent=major,
            )
        )

        result.severity = severity
        result.impact = impact
        result.confidence = confidence

        return result