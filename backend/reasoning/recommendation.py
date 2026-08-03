"""
GeoGuard AI

Recommendation Parser

Author: Shivam Salve
"""

import json

from backend.assessment.result import AssessmentResult
from backend.reasoning.result import ReasoningResult


class RecommendationEngine:
    """
    Converts Gemma JSON output into
    a ReasoningResult.
    """

    @staticmethod
    def parse(
        response: str,
        assessment: AssessmentResult,
    ) -> ReasoningResult:

        result = ReasoningResult()

        try:

            data = json.loads(response)

            result.summary = data.get(
                "summary",
                "",
            )

            result.analysis = data.get(
                "analysis",
                "",
            )

            result.priority = data.get(
                "priority",
                "Unknown",
            )

            result.recommendations = data.get(
                "recommendations",
                [],
            )

        except Exception:

            result.summary = response

            result.analysis = response

            result.priority = "Unknown"

            result.recommendations = []

        # -----------------------------
        # Copy Assessment Information
        # -----------------------------

        result.severity = assessment.severity

        result.impact = assessment.impact

        result.confidence = assessment.confidence

        return result