"""
GeoGuard AI

Dependency Test

Author: Shivam Salve
"""

from backend.api.dependencies import get_engine


engine1 = get_engine()

engine2 = get_engine()

print("=" * 70)

print(engine1 is engine2)

print("=" * 70)