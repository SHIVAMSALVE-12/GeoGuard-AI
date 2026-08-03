from pathlib import Path

from backend.geoguard.engine import GeoGuardEngine
from backend.assessment.engine import AssessmentEngine


geo = GeoGuardEngine()

assessment = AssessmentEngine()

geo_result = geo.predict(

    damage_image=Path(
        "backend/datasets/test_damage.png"
    )

)

result = assessment.build(
    geo_result
)

print("=" * 70)

print(result)

print("=" * 70)