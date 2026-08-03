"""
GeoGuard AI

Disaster Severity Calculator

Author: Shivam Salve
"""


class SeverityCalculator:
    """
    Computes overall disaster severity
    using flood and building damage statistics.
    """

    @staticmethod
    def calculate(
        flooded_percent: float,
        destroyed_percent: float,
        major_damage_percent: float,
    ) -> tuple[str, str, float]:

        score = 0

        # -----------------------------------------
        # Flood Contribution
        # -----------------------------------------

        if flooded_percent >= 40:

            score += 4

        elif flooded_percent >= 20:

            score += 3

        elif flooded_percent >= 10:

            score += 2

        elif flooded_percent > 0:

            score += 1

        # -----------------------------------------
        # Destroyed Buildings
        # -----------------------------------------

        if destroyed_percent >= 20:

            score += 4

        elif destroyed_percent >= 10:

            score += 3

        elif destroyed_percent >= 5:

            score += 2

        elif destroyed_percent > 0:

            score += 1

        # -----------------------------------------
        # Major Damage
        # -----------------------------------------

        if major_damage_percent >= 20:

            score += 3

        elif major_damage_percent >= 10:

            score += 2

        elif major_damage_percent > 0:

            score += 1

        # -----------------------------------------
        # Overall Severity
        # -----------------------------------------

        if score >= 10:

            severity = "Extreme"

            impact = "Catastrophic"

        elif score >= 7:

            severity = "High"

            impact = "Severe"

        elif score >= 4:

            severity = "Moderate"

            impact = "Significant"

        elif score >= 1:

            severity = "Low"

            impact = "Limited"

        else:

            severity = "Minimal"

            impact = "Negligible"

        confidence = min(
            100.0,
            score * 10.0,
        )

        return (
            severity,
            impact,
            confidence,
        )