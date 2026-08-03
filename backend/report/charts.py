"""
GeoGuard AI

Charts & Statistics Generator

Author: Shivam Salve
"""

from pathlib import Path

import matplotlib.pyplot as plt

from backend.assessment.result import AssessmentResult


class ChartGenerator:
    """
    Generates professional charts for reports.
    """

    def __init__(self):

        self.output_dir = Path(
            "backend/outputs/reports/charts"
        )

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    # =====================================================
    # Damage Pie Chart
    # =====================================================

    def damage_chart(
        self,
        assessment: AssessmentResult,
    ) -> str:

        labels = []
        values = []

        for key, value in assessment.damage.items():

            labels.append(key)

            values.append(value)

        fig = plt.figure(figsize=(6, 6))

        plt.pie(
            values,
            labels=labels,
            autopct="%1.1f%%",
            startangle=90,
        )

        plt.title(
            "Building Damage Distribution"
        )

        path = self.output_dir / "damage_pie.png"

        plt.savefig(
            path,
            dpi=200,
            bbox_inches="tight",
        )

        plt.close(fig)

        return str(path)

    # =====================================================
    # Flood Pie Chart
    # =====================================================

    def flood_chart(
        self,
        assessment: AssessmentResult,
    ) -> str | None:

        if not assessment.flood:

            return None

        labels = list(
            assessment.flood.keys()
        )

        values = list(
            assessment.flood.values()
        )

        fig = plt.figure(figsize=(6, 6))

        plt.pie(
            values,
            labels=labels,
            autopct="%1.1f%%",
            startangle=90,
        )

        plt.title(
            "Flood Distribution"
        )

        path = self.output_dir / "flood_pie.png"

        plt.savefig(
            path,
            dpi=200,
            bbox_inches="tight",
        )

        plt.close(fig)

        return str(path)

    # =====================================================
    # Land Cover Bar Chart
    # =====================================================

    def landcover_chart(
        self,
        assessment: AssessmentResult,
    ) -> str | None:

        if not assessment.landcover:

            return None

        labels = list(
            assessment.landcover.keys()
        )

        values = list(
            assessment.landcover.values()
        )

        fig = plt.figure(figsize=(8, 5))

        plt.bar(
            labels,
            values,
        )

        plt.ylabel("Percentage")

        plt.title(
            "Land Cover Distribution"
        )

        plt.xticks(rotation=25)

        path = (
            self.output_dir
            / "landcover_bar.png"
        )

        plt.savefig(
            path,
            dpi=200,
            bbox_inches="tight",
        )

        plt.close(fig)

        return str(path)

    # =====================================================
    # Confidence Bar
    # =====================================================

    def confidence_chart(
        self,
        assessment: AssessmentResult,
    ) -> str:

        fig = plt.figure(figsize=(6, 1.8))

        plt.barh(
            ["Confidence"],
            [assessment.confidence],
        )

        plt.xlim(0, 100)

        plt.title("AI Confidence")

        path = (
            self.output_dir
            / "confidence.png"
        )

        plt.savefig(
            path,
            dpi=200,
            bbox_inches="tight",
        )

        plt.close(fig)

        return str(path)