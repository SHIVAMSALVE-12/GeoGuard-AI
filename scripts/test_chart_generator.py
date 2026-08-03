"""
GeoGuard AI

Chart Generator Test

Author: Shivam Salve
"""

from pathlib import Path

from backend.geoguard.engine import GeoGuardEngine
from backend.report.charts import ChartGenerator


def main():

    engine = GeoGuardEngine()

    result = engine.predict(

        damage_image=Path(
            "backend/datasets/test_damage.png"
        )

    )

    charts = ChartGenerator()

    damage = charts.damage_chart(
        result.assessment
    )

    flood = charts.flood_chart(
        result.assessment
    )

    landcover = charts.landcover_chart(
        result.assessment
    )

    confidence = charts.confidence_chart(
        result.assessment
    )

    print("=" * 70)

    print("Damage Chart     :", damage)

    print("Flood Chart      :", flood)

    print("Land Cover Chart :", landcover)

    print("Confidence Chart :", confidence)

    print("=" * 70)


if __name__ == "__main__":

    main()