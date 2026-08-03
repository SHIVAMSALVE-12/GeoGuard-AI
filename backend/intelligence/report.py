"""
GeoGuard AI

Disaster Report Generator

Author: Shivam Salve
"""

from pathlib import Path


class DisasterReportGenerator:
    """
    Generates a professional disaster assessment report.
    """

    def __init__(self):
        pass

    def generate(
        self,
        assessment,
        land_cover,
    ):

        lines = []

        lines.append("=" * 60)
        lines.append("GeoGuard AI Disaster Assessment Report")
        lines.append("=" * 60)

        lines.append("")
        lines.append("Assessment")
        lines.append("-" * 30)
        lines.append(f"Severity     : {assessment.severity}")
        lines.append(f"Risk Score   : {assessment.risk_score}")

        lines.append("")
        lines.append("Land Cover")
        lines.append("-" * 30)
        lines.append(
            f"Dominant Class : {land_cover.dominant_class}"
        )

        lines.append("")
        lines.append("AI Findings")
        lines.append("-" * 30)
        lines.append(assessment.summary)

        lines.append("")
        lines.append("Recommendations")
        lines.append("-" * 30)

        for recommendation in assessment.recommendations:

            lines.append(f"✓ {recommendation}")

        lines.append("")
        lines.append("=" * 60)

        return "\n".join(lines)

    def save(
        self,
        report,
        output_path,
    ):

        output_path = Path(output_path)

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with open(
            output_path,
            "w",
            encoding="utf-8",
        ) as file:

            file.write(report)

        print(f"✅ Report saved -> {output_path}")