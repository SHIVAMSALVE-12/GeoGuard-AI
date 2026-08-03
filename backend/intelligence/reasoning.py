"""
GeoGuard AI

AI Reasoning Engine

Author: Shivam Salve
"""

from backend.intelligence.schemas import (
    DisasterAssessment,
)

from backend.intelligence.severity import (
    SeverityEngine,
)

from backend.intelligence.recommendation import RecommendationEngine


class AIReasoningEngine:
    """
    AI Reasoning Engine

    Combines outputs from multiple AI models
    and generates a disaster assessment.
    """

    def __init__(self):

        self.severity_engine = SeverityEngine()
        self.recommendation_engine = RecommendationEngine()
    def analyze(
        self,
        fused_results,
    ):
        """
        Analyze fused AI model outputs.

        Parameters
        ----------
        fused_results : dict

        Returns
        -------
        DisasterAssessment
        """

        land = fused_results["land_cover"]
        flood = fused_results["flood"]
        damage = fused_results["damage"]
        change = fused_results["change"]

        assessment = DisasterAssessment()

        # ----------------------------------------------------
        # Calculate Severity
        # ----------------------------------------------------

        score, severity = self.severity_engine.calculate(
            flood=flood,
            damage=damage,
            change=change,
        )

        # ----------------------------------------------------
        # Generate Summary
        # ----------------------------------------------------

        summary = []

        summary.append(
            f"Dominant land cover: {land.dominant_class}"
        )

        if flood is not None and flood.flood_detected:

            summary.append(
                f"Flood detected over "
                f"{flood.flooded_area_percent:.1f}% of the area."
            )

        if damage is not None and damage.buildings_damaged > 0:

            summary.append(
                f"{damage.buildings_damaged} damaged buildings detected."
            )

        if change is not None and change.change_detected:

            summary.append(
                f"Land change detected across "
                f"{change.changed_area_percent:.1f}% of the area."
            )

        # ----------------------------------------------------
        # Generate Recommendations
        # ----------------------------------------------------

        recommendations = self.recommendation_engine.generate(
        flood=flood,
        damage=damage,
        change=change,
        )

        # ----------------------------------------------------
        # Populate Assessment
        # ----------------------------------------------------

        assessment.severity = severity

        assessment.risk_score = score

        assessment.summary = "\n".join(summary)

        assessment.recommendations = recommendations

        return assessment