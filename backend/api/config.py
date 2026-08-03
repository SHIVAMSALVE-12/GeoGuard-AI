"""
GeoGuard AI

API Configuration

Author: Shivam Salve
"""

from pathlib import Path


class Settings:

    PROJECT_NAME = "GeoGuard AI"

    VERSION = "1.0.0"

    API_PREFIX = "/api"

    OUTPUT_DIR = Path(
        "backend/outputs"
    )

    REPORT_DIR = OUTPUT_DIR / "reports"

    MAX_UPLOAD_SIZE = 100 * 1024 * 1024


settings = Settings()