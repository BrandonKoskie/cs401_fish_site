"""
Database seeding script for the Hawaii Seafood Guide.

This script populates the SQLite database with initial data for:
- Overfished areas in Hawaii
- Imported seafood species
- Sustainable fishing methods

Usage:
    python seed.py
"""
import sys
sys.path.insert(0, '.')

from api.app import app
from api.models import db, OverfishedArea, ImportedSpecies, FishingMethod

# ── Overfished Areas Data ─────────────────────────────────────────────────
OVERFISHED_AREAS = [
    {
        "area": "Oahu South Shore (Waikiki area)",
        "overfishing_status": "High pressure / Declining",
        "main_reasons": "Heavy recreational + commercial fishing, pollution",
        "source_link": "DLNR DAR Reports"
    },
    {
        "area": "West Hawaii (Big Island Kona)",
        "overfishing_status": "Moderate-High",
        "main_reasons": "Tourism pressure, spearfishing, habitat loss",
        "source_link": "NOAA Coral Reef Task Force"
    },
    {
        "area": "Maui Reef Areas",
        "overfishing_status": "Declining in many zones",
        "main_reasons": "Overfishing of reef herbivores, coral bleaching",
        "source_link": "Hawaii Coral Reef Strategy"
    },
    {
        "area": "Main Hawaiian Islands (general)",
        "overfishing_status": "High",
        "main_reasons": "Combined commercial + recreational pressure",
        "source_link": "NOAA Fisheries Assessment"
    },
    {
        "area": "Northwestern Hawaiian Islands",
        "overfishing_status": "Mostly Protected / Healthy",
        "main_reasons": "Marine National Monument restrictions",
        "source_link": "Papahānaumokuākea"
    },
    {
        "area": "Kaneohe Bay (Oahu)",
        "overfishing_status": "High local pressure",
        "main_reasons": "Lay netting, pollution, habitat degradation",
        "source_link": "DLNR Marine Lab Refuge"
    },
]

# ── Imported Species Data ─────────────────────────────────────────────────
IMPORTED_SPECIES = [
    {
        "species": "Shrimp",
        "annual_import_volume": "Very High",
        "main_reason": "High local demand, limited local supply",
        "source_link": "USDA FAS / Hawaii Ag Data"
    },
    {
        "species": "Atlantic Salmon",
        "annual_import_volume": "High",
        "main_reason": "Popular for restaurants and retail",
        "source_link": "Hawaii Seafood Imports Report"
    },
    {
        "species": "Tilapia",
        "annual_import_volume": "Medium-High",
        "main_reason": "Affordable farmed protein",
        "source_link": "NOAA Trade Data"
    },
    {
        "species": "Canned Tuna",
        "annual_import_volume": "High",
        "main_reason": "Convenience and cost",
        "source_link": "Hawaii Import Statistics"
    },
    {
        "species": "Frozen Yellowfin Tuna",
        "annual_import_volume": "Medium",
        "main_reason": "Supplement to local catch",
        "source_link": "NOAA Pacific Islands"
    },
    {
        "species": "Cod / Pollock",
        "annual_import_volume": "Medium",
        "main_reason": "Used in processed foods",
        "source_link": "USDA Foreign Agricultural Service"
    },
]

# ── Fishing Methods Data ──────────────────────────────────────────────────
FISHING_METHODS = [
    {
        "method": "Spearfishing (free dive)",
        "description": "Selective targeting of individual fish with spear gun or pole spear",
        "sustainability_rank": "High (Very Sustainable)",
        "key_reasons": "Low bycatch, only take what you need",
        "source_link": "DLNR DAR"
    },
    {
        "method": "Pole-and-Line / Trolling",
        "description": "Hook and line from boat, often one fish at a time",
        "sustainability_rank": "High",
        "key_reasons": "Low bycatch, Hawaii troll fisheries well-managed",
        "source_link": "Seafood Watch Hawaii Guide"
    },
    {
        "method": "Handline",
        "description": "Traditional line fishing from shore or small boat",
        "sustainability_rank": "High",
        "key_reasons": "Very selective, minimal habitat impact",
        "source_link": "NOAA Pacific Islands"
    },
    {
        "method": "Trap Fishing (fish traps)",
        "description": "Baited traps placed on reef or bottom",
        "sustainability_rank": "Medium-High",
        "key_reasons": "Can be selective if properly designed",
        "source_link": "DLNR Fishing Regulations"
    },
    {
        "method": "Longline Fishing",
        "description": "Long lines with many hooks (commercial)",
        "sustainability_rank": "Medium (varies)",
        "key_reasons": "Some Hawaii longline certified sustainable, bycatch risk",
        "source_link": "NOAA Fisheries"
    },
    {
        "method": "Purse Seine",
        "description": "Large nets that encircle schools of fish",
        "sustainability_rank": "Low",
        "key_reasons": "High bycatch of non-target species",
        "source_link": "Seafood Watch"
    },
    {
        "method": "Lay Netting / Gill Net",
        "description": "Nets that entangle fish by the gills",
        "sustainability_rank": "Very Low",
        "key_reasons": "Highly damaging to reefs and non-target species",
        "source_link": "DLNR Regulations"
    },
    {
        "method": "Cast Net / Throw Net",
        "description": "Hand-thrown net for baitfish or small species",
        "sustainability_rank": "Medium",
        "key_reasons": "Selective when used responsibly",
        "source_link": "Traditional Hawaiian methods"
    },
    {
        "method": "Diving with SCUBA",
        "description": "Spearfishing with tanks (deeper access)",
        "sustainability_rank": "Low-Medium",
        "key_reasons": "Can lead to overfishing of deeper reefs",
        "source_link": "Hawaii Reef Sustainability Reports"
    },
    {
        "method": "Aquaculture (farmed)",
        "description": "Farm-raised fish (e.g., tilapia, some shrimp)",
        "sustainability_rank": "Varies (often High)",
        "key_reasons": "Reduces pressure on wild stocks",
        "source_link": "NOAA & Hawaii Seafood Council"
    },
]


def seed_database():
    """
    Seed the database with initial data for overfished areas, imported
    species, and fishing methods.
    
    Creates all database tables and populates them with the predefined
    data arrays above. Uses the Flask application context to ensure
    proper database connection.
    """
    with app.app_context():
        # db.drop_all()  # COMMENTED - was destroying data
        # db.create_all()  # COMMENTED - was destroying data
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
