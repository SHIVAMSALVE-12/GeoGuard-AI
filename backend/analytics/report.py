"""
GeoGuard AI

AI Report Generator

Author: Shivam Salve
"""

from pathlib import Path


class ReportGenerator:

    def __init__(self):
        pass

    def generate(self, stats):

        report = []

        report.append("=" * 60)
        report.append("GeoGuard AI Analysis Report")
        report.append("=" * 60)

        report.append("")
        report.append("Image Information")
        report.append("-" * 30)

        report.append(f"Width          : {stats['width']} px")
        report.append(f"Height         : {stats['height']} px")
        report.append(f"Pixels         : {stats['total_pixels']}")

        report.append("")
        report.append("Detected Land Cover")
        report.append("-" * 30)

        for name, percent in stats["percentages"].items():

            report.append(
                f"{name:<15}: {percent:.2f}%"
            )

        report.append("")
        report.append("Dominant Class")
        report.append("-" * 30)

        report.append(stats["dominant_class"])

        report.append("")
        report.append("AI Summary")
        report.append("-" * 30)

        summary = self.generate_summary(stats)

        report.extend(summary)

        report.append("")
        report.append("=" * 60)

        return "\n".join(report)

    def generate_summary(self, stats):

        summary = []

        dominant = stats["dominant_class"]

        if dominant == "Tree":

            summary.append(
                "The satellite image is dominated by vegetation."
            )

        elif dominant == "Buildings":

            summary.append(
                "The area appears to be highly urbanized."
            )

        elif dominant == "Water":

            summary.append(
                "The image contains significant water coverage."
            )

        elif dominant == "Grass":

            summary.append(
                "Large grassland areas are present."
            )

        elif dominant == "Cropland":

            summary.append(
                "Agricultural land is the dominant feature."
            )

        elif dominant == "Road":

            summary.append(
                "Road infrastructure occupies a significant area."
            )

        elif dominant == "Bareland":

            summary.append(
                "Large barren land regions are detected."
            )

        if stats["percentages"].get("Water", 0) > 20:

            summary.append(
                "A large amount of surface water is present."
            )

        if stats["percentages"].get("Buildings", 0) > 25:

            summary.append(
                "Dense built-up regions are detected."
            )

        if stats["percentages"].get("Tree", 0) > 40:

            summary.append(
                "Heavy vegetation cover is visible."
            )

        return summary

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

        print(
            f"✅ Report saved -> {output_path}"
        )