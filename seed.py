"""
Database seeding script for the Hawaii Seafood Guide.

This script populates the SQLite database with initial data from seed_data.py.
Can be run manually or automatically on first app startup.

Usage:
    python seed.py
"""
import sys
sys.path.insert(0, '.')

from api.app import app
from api.models import db, OverfishedArea, ImportedSpecies, FishingMethod
from seed_data import OVERFISHED_AREAS, IMPORTED_SPECIES, FISHING_METHODS


def seed_database():
    """
    Seed the database with initial data for overfished areas, imported
    species, and fishing methods.
    """
    with app.app_context():
        db.create_all()
        for item in OVERFISHED_AREAS:
            db.session.add(OverfishedArea(**item))
        for item in IMPORTED_SPECIES:
            db.session.add(ImportedSpecies(**item))
        for item in FISHING_METHODS:
            db.session.add(FishingMethod(**item))
        db.session.commit()
        print(f"Seeded {len(OVERFISHED_AREAS)} overfished areas")
        print(f"Seeded {len(IMPORTED_SPECIES)} imported species")
        print(f"Seeded {len(FISHING_METHODS)} fishing methods")


if __name__ == "__main__":
    seed_database()
