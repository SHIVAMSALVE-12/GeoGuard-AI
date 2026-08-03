"""
GeoGuard AI

Logger Test

Author: Shivam Salve
"""

from backend.logs.logger import logger


logger.info("GeoGuard AI Started")

logger.warning("This is a warning.")

logger.error("This is an error.")

print("=" * 60)
print("Logging Test Completed")
print("=" * 60)