"""
GeoGuard AI

Prediction API

Author: Shivam Salve
"""

import shutil
import tempfile
import traceback
from pathlib import Path

from fastapi import APIRouter
from fastapi import Depends
from fastapi import File
from fastapi import HTTPException
from fastapi import Request
from fastapi import UploadFile

from backend.api.dependencies import get_engine
from backend.api.schemas import (
    AssessmentSchema,
    FilesSchema,
    PredictionResponse,
    ReasoningSchema,
)
from backend.geoguard.engine import GeoGuardEngine


router = APIRouter()


@router.post(
    "/predict",
    response_model=PredictionResponse,
    summary="Run AI Disaster Assessment",
    description="""
Upload a satellite or aerial disaster image.

GeoGuard AI performs:

- Building Damage Detection
- Disaster Assessment
- AI Reasoning using Gemma 2

Returns structured JSON results.
""",
)
async def predict_damage(
    request: Request,
    image: UploadFile = File(...),
    engine: GeoGuardEngine = Depends(get_engine),
):
    """
    Upload an image and run GeoGuard AI.
    """

    # =====================================================
    # Validate Upload
    # =====================================================

    if image.filename is None:
        raise HTTPException(
            status_code=400,
            detail="No filename received.",
        )

    suffix = Path(image.filename).suffix.lower()

    allowed_extensions = {
        ".png",
        ".jpg",
        ".jpeg",
        ".tif",
        ".tiff",
    }

    if suffix not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported image format: {suffix}",
        )

    # =====================================================
    # Save Uploaded Image
    # =====================================================

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix,
    ) as tmp:

        shutil.copyfileobj(
            image.file,
            tmp,
        )

        temp_path = Path(tmp.name)

    try:

        # =====================================================
        # Run GeoGuard AI
        # =====================================================

        result = engine.predict(
            damage_image=temp_path,
        )

        # =====================================================
        # Validate AI Output
        # =====================================================

        if result.assessment is None:
            raise HTTPException(
                status_code=500,
                detail="Assessment was not generated.",
            )

        if result.reasoning is None:
            raise HTTPException(
                status_code=500,
                detail="Reasoning was not generated.",
            )

        # =====================================================
        # Base URL
        # =====================================================

        base_url = str(request.base_url).rstrip("/")

        # =====================================================
        # Assessment
        # =====================================================

        assessment = AssessmentSchema(

            severity=result.assessment.severity,

            impact=result.assessment.impact,

            confidence=result.assessment.confidence,

            landcover=result.assessment.landcover,

            flood=result.assessment.flood,

            damage=result.assessment.damage,

        )

        # =====================================================
        # Reasoning
        # =====================================================

        reasoning = ReasoningSchema(

            summary=result.reasoning.summary,

            analysis=result.reasoning.analysis,

            priority=result.reasoning.priority,

            recommendations=result.reasoning.recommendations,

        )

        # =====================================================
        # Generated Files
        # =====================================================

        files = FilesSchema()

        if result.damage is not None:

            if result.damage.prediction_path:

                files.prediction = (
                    f"{base_url}/api/download/"
                    f"{Path(result.damage.prediction_path).name}"
                )

            if result.damage.overlay_path:

                files.overlay = (
                    f"{base_url}/api/download/"
                    f"{Path(result.damage.overlay_path).name}"
                )

        # =====================================================
        # Optional Reports
        # =====================================================

        if hasattr(result, "report") and result.report:

            if result.report.html_path:

                files.html_report = (
                    f"{base_url}/api/download/"
                    f"{Path(result.report.html_path).name}"
                )

            if result.report.pdf_path:

                files.pdf_report = (
                    f"{base_url}/api/download/"
                    f"{Path(result.report.pdf_path).name}"
                )

        # =====================================================
        # Response
        # =====================================================

        return PredictionResponse(

            success=True,

            message="Prediction completed successfully.",

            assessment=assessment,

            reasoning=reasoning,

            files=files,

        )

    except HTTPException:
        raise

    except Exception as e:

        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )

    finally:

        if temp_path.exists():

            temp_path.unlink()