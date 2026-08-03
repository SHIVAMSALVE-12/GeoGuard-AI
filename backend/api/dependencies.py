"""
GeoGuard AI

FastAPI Dependencies

Author: Shivam Salve
"""

from functools import lru_cache

from backend.geoguard.engine import GeoGuardEngine


@lru_cache(maxsize=1)
def get_engine() -> GeoGuardEngine:
    """
    Returns a singleton GeoGuardEngine.

    The AI models are loaded once and reused
    for every API request.
    """

    return GeoGuardEngine()