"""
GeoGuard AI

Gemma Prompt Builder

Author: Shivam Salve
"""

from backend.assessment.result import AssessmentResult


class PromptBuilder:
    """
    Converts an AssessmentResult into a structured prompt
    for Gemma 2.

    The prompt requests a strict JSON response so that
    GeoGuard can reliably parse the output.
    """

    @staticmethod
    def build(
        assessment: AssessmentResult,
    ) -> str:

        lines = []

        # =====================================================
        # Header
        # =====================================================

        lines.append(
            "You are GeoGuard AI, an expert disaster assessment assistant."
        )

        lines.append(
            "Analyze the disaster assessment below."
        )

        lines.append("")

        # =====================================================
        # Land Cover
        # =====================================================

        if assessment.landcover:

            lines.append("LAND COVER")
            lines.append("-" * 40)

            for key, value in assessment.landcover.items():

                lines.append(
                    f"{key}: {value:.2f}%"
                )

            lines.append("")

        # =====================================================
        # Flood
        # =====================================================

        if assessment.flood:

            lines.append("FLOOD")
            lines.append("-" * 40)

            for key, value in assessment.flood.items():

                lines.append(
                    f"{key}: {value:.2f}%"
                )

            lines.append("")

        # =====================================================
        # Building Damage
        # =====================================================

        if assessment.damage:

            lines.append("BUILDING DAMAGE")
            lines.append("-" * 40)

            for key, value in assessment.damage.items():

                lines.append(
                    f"{key}: {value:.2f}%"
                )

            lines.append("")

        # =====================================================
        # Overall Assessment
        # =====================================================

        lines.append("OVERALL ASSESSMENT")
        lines.append("-" * 40)

        lines.append(
            f"Severity: {assessment.severity}"
        )

        lines.append(
            f"Impact: {assessment.impact}"
        )

        lines.append(
            f"Confidence: {assessment.confidence:.1f}%"
        )

        lines.append("")

        # =====================================================
        # Instructions
        # =====================================================

        lines.append(
            "Generate a disaster intelligence report."
        )

        lines.append("")

        lines.append(
            "Return ONLY valid JSON."
        )

        lines.append(
            "Do NOT return markdown."
        )

        lines.append(
            "Do NOT use code fences."
        )

        lines.append(
            "Do NOT explain anything outside the JSON."
        )

        lines.append("")

        # =====================================================
        # JSON Schema
        # =====================================================

        lines.append("{")
        lines.append('    "summary": "string",')
        lines.append('    "analysis": "string",')
        lines.append('    "priority": "Low | Medium | High | Critical",')
        lines.append('    "recommendations": [')
        lines.append('        "recommendation 1",')
        lines.append('        "recommendation 2",')
        lines.append('        "recommendation 3",')
        lines.append('        "recommendation 4"')
        lines.append("    ]")
        lines.append("}")

        return "\n".join(lines)