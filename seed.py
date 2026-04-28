import sys
sys.path.insert(0, '.')

from api.app import app
from api.models import db, OverfishedArea, ImportedSpecies, FishingMethod, ConsumerGuide

OVERFISHED_AREAS = [
    {"area": "Oahu South Shore (Waikiki area)", "overfishing_status": "High pressure / Declining", "main_reasons": "Heavy recreational + commercial fishing, pollution", "source_link": "DLNR DAR Reports"},
    {"area": "West Hawaii (Big Island Kona)", "overfishing_status": "Moderate-High", "main_reasons": "Tourism pressure, spearfishing, habitat loss", "source_link": "NOAA Coral Reef Task Force"},
    {"area": "Maui Reef Areas", "overfishing_status": "Declining in many zones", "main_reasons": "Overfishing of reef herbivores, coral bleaching", "source_link": "Hawaii Coral Reef Strategy"},
    {"area": "Main Hawaiian Islands (general)", "overfishing_status": "High", "main_reasons": "Combined commercial + recreational pressure", "source_link": "NOAA Fisheries Assessment"},
    {"area": "Northwestern Hawaiian Islands", "overfishing_status": "Mostly Protected / Healthy", "main_reasons": "Marine National Monument restrictions", "source_link": "Papahanaumokuakea"},
    {"area": "Kaneohe Bay (Oahu)", "overfishing_status": "High local pressure", "main_reasons": "Lay netting, pollution, habitat degradation", "source_link": "DLNR Marine Lab Refuge"},
]

IMPORTED_SPECIES = [
    {"species": "Shrimp", "annual_import_volume": "Very High", "main_reason": "High local demand, limited local supply", "source_link": "USDA FAS / Hawaii Ag Data"},
    {"species": "Atlantic Salmon", "annual_import_volume": "High", "main_reason": "Popular for restaurants and retail", "source_link": "Hawaii Seafood Imports Report"},
    {"species": "Tilapia", "annual_import_volume": "Medium-High", "main_reason": "Affordable farmed protein", "source_link": "NOAA Trade Data"},
    {"species": "Canned Tuna", "annual_import_volume": "High", "main_reason": "Convenience and cost", "source_link": "Hawaii Import Statistics"},
    {"species": "Frozen Yellowfin Tuna", "annual_import_volume": "Medium", "main_reason": "Supplement to local catch", "source_link": "NOAA Pacific Islands"},
    {"species": "Cod / Pollock", "annual_import_volume": "Medium", "main_reason": "Used in processed foods", "source_link": "USDA Foreign Agricultural Service"},
]

FISHING_METHODS = [
    {"method": "Spearfishing (free dive)", "description": "Selective targeting of individual fish with spear gun or pole spear", "sustainability_rank": "High (Very Sustainable)", "key_reasons": "Low bycatch, only take what you need", "source_link": "DLNR DAR"},
    {"method": "Pole-and-Line / Trolling", "description": "Hook and line from boat, often one fish at a time", "sustainability_rank": "High", "key_reasons": "Low bycatch, Hawaii troll fisheries well-managed", "source_link": "Seafood Watch Hawaii Guide"},
    {"method": "Handline", "description": "Traditional line fishing from shore or small boat", "sustainability_rank": "High", "key_reasons": "Very selective, minimal habitat impact", "source_link": "NOAA Pacific Islands"},
    {"method": "Trap Fishing (fish traps)", "description": "Baited traps placed on reef or bottom", "sustainability_rank": "Medium-High", "key_reasons": "Can be selective if properly designed", "source_link": "DLNR Fishing Regulations"},
    {"method": "Longline Fishing", "description": "Long lines with many hooks (commercial)", "sustainability_rank": "Medium (varies)", "key_reasons": "Some Hawaii longline certified sustainable, bycatch risk", "source_link": "NOAA Fisheries"},
    {"method": "Purse Seine", "description": "Large nets that encircle schools of fish", "sustainability_rank": "Low", "key_reasons": "High bycatch of non-target species", "source_link": "Seafood Watch"},
    {"method": "Lay Netting / Gill Net", "description": "Nets that entangle fish by the gills", "sustainability_rank": "Very Low", "key_reasons": "Highly damaging to reefs and non-target species", "source_link": "DLNR Regulations"},
    {"method": "Cast Net / Throw Net", "description": "Hand-thrown net for baitfish or small species", "sustainability_rank": "Medium", "key_reasons": "Selective when used responsibly", "source_link": "Traditional Hawaiian methods"},
    {"method": "Diving with SCUBA", "description": "Spearfishing with tanks (deeper access)", "sustainability_rank": "Low-Medium", "key_reasons": "Can lead to overfishing of deeper reefs", "source_link": "Hawaii Reef Sustainability Reports"},
    {"method": "Aquaculture (farmed)", "description": "Farm-raised fish (e.g., tilapia, some shrimp)", "sustainability_rank": "Varies (often High)", "key_reasons": "Reduces pressure on wild stocks", "source_link": "NOAA & Hawaii Seafood Council"},
]

CONSUMER_GUIDES = [
    {"guide_name": "Top Sustainable Poke Fish", "description": "Find enviornmentally friendly fish commonly used in poke bowls", "content": "Recommended species: Ahi, Salmon. Tip: Choose locally caught fish to reduce environmental impact. Recipe idea: Build a poke bowl with rice as a base, add cubed salmon or tuna, and optional toppings like seaweed, cucumber, and furikake for extra flavor.","filters": "poke, ahi, popular",
        "resources": " NOAA Sustainable Seafood"},
    {"guide_name": "Low Mercury Options for Families", "description": "Provides safe seafood choices for children and pregnant women.", "content": "Recommended species: Salmon (Low mercury), Sardines (Low mercury), Shrimp (Very low mercury), Tilapia. Tip: To avoid high-mercury fish like swordfish and bigeye tuna. Recipe idea: Grilled salmon with lemon.", "filters": "low mercury, health", "resources": "FDA Seafood Consumption"},
    {"guide_name": "Budget Friendly Healthy Seafood Options", "description": "Affordable seafood options that are healthy and widely available.", "content": "Recommended species: Canned light tuna, Sardines, Pollock. Tip: Frozen and canned options are often cheaper but still nutritious. Recipe idea: Tuna sandwich - add mayonnaise and chopped celery to canned tuna.", "filters": "budget, low cost, easy meals", "resources": "USDA Seafood Nutrition"},
    {"guide_name": "Seasonal Seafood Guide", "description": "Shows the best seasonal seafood options to support sustainable fishing.", "content": "Recommended seasonal fish: Ahi (year around), Mahi Mahi (spring and summer), Shrimp (year around). Tip: Eating in-season seafood reduces pressure on fish populations. Recipe idea: Seafood and white rice", "filters": "seasonal, fish, sustainable", "resources": "Hawaii Division of Aquatic Resources"},
    {"guide_name": "Beginner’s Guide to Sustainable Seafood", "description": "Introduces beginners to making seafood choices.", "content": "Recommended species: Salmon, Tuna, Shrimp. Tip: Look for seafood certified by sustainability programs. Recipe idea: Simple baked salmon with vegetables.", "filters": "beginner, sustainable, easy", "resources": "Seafood Watch Beginner Guide"},
    {"guide_name": "Healthy Grilling & Cooking Seafood Guide", "description": "Healthy cooking methods for seafood and seafood preparation techniques.", "content": "Recommended species: Salmon, Mahi-Mahi, Shrimp. Tip: Grilling and baking preserve nutrients and reduce added fats. Recipe idea: Grilled mahi-mahi tacos with cabbage slaw.", "filters": "cooked, grilling, recipes", "resources": "NOAA Cooking Guide"}
]

with app.app_context():
    db.drop_all()
    db.create_all()
    for item in OVERFISHED_AREAS:
        db.session.add(OverfishedArea(**item))
    for item in IMPORTED_SPECIES:
        db.session.add(ImportedSpecies(**item))
    for item in FISHING_METHODS:
        db.session.add(FishingMethod(**item))
    for item in CONSUMER_GUIDES:
        db.session.add(ConsumerGuide(**item))
    db.session.commit()
    print(f"Seeded {len(OVERFISHED_AREAS)} overfished areas")
    print(f"Seeded {len(IMPORTED_SPECIES)} imported species")
    print(f"Seeded {len(FISHING_METHODS)} fishing methods")
    print(f"Seedes {len(CONSUMER_GUIDES)} consumer guides")


