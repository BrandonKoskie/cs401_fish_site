from flask import Blueprint, jsonify, abort, request, render_template
from api.models import db
from api.models import OverfishedArea, ImportedSpecies, FishingMethod, ConsumerGuide

api_bp = Blueprint('api', __name__)

# ── Fish Species (Brandon's existing code) ────────────────────────────────────

@api_bp.route('/basics')
def basics_page():
    return render_template('seafood_basics.html')

@api_bp.route('/fish')
def fish_page():
    return render_template('local_fish.html')

fish_species = [
    {"id": 1, "common_name": "Ahi", "scientific_name": "Thunnus albacares", "sustainability_rating": "Good Alternative", "health_notes": "Moderate mercury levels. Pregnant women and children should limit intake.", "preparation": "Popular for poke, sashimi, and grilling.", "description": "Yellowfin tuna is one of the most important commercial fish in Hawaii.", "image_url": "https://via.placeholder.com/400x300?text=Ahi"},
    {"id": 2, "common_name": "Mahimahi", "scientific_name": "Coryphaena hippurus", "sustainability_rating": "Best Choice", "health_notes": "Low mercury. High in protein and omega-3s.", "preparation": "Excellent for grilling, fish tacos, and ceviche.", "description": "Also known as dolphinfish, a fast-swimming pelagic species.", "image_url": "https://via.placeholder.com/400x300?text=Mahimahi"},
    {"id": 3, "common_name": "Opakapaka", "scientific_name": "Pristipomoides filamentosus", "sustainability_rating": "Good Alternative", "health_notes": "Moderate mercury. Highly prized for fine dining.", "preparation": "Steamed or baked with ginger and green onions.", "description": "Pink snapper is a deep-water species valued for its delicate flavor.", "image_url": "https://via.placeholder.com/400x300?text=Opakapaka"},
    {"id": 4, "common_name": "Uku", "scientific_name": "Aprion virescens", "sustainability_rating": "Good Alternative", "health_notes": "Low to moderate mercury.", "preparation": "Fried or steamed.", "description": "Green jobfish, a common deep-water species in Hawaii.", "image_url": "https://via.placeholder.com/400x300?text=Uku"},
    {"id": 5, "common_name": "Onaga", "scientific_name": "Etelis coruscans", "sustainability_rating": "Best Choice", "health_notes": "Low mercury. Popular in upscale restaurants.", "preparation": "Steamed or lightly seared.", "description": "Longtail snapper, prized for its firm white flesh.", "image_url": "https://via.placeholder.com/400x300?text=Onaga"},
    {"id": 6, "common_name": "Kole", "scientific_name": "Ctenochaetus strigosus", "sustainability_rating": "Sustainable", "health_notes": "Low mercury.", "preparation": "Fried or grilled.", "description": "Goldring surgeonfish, a common reef herbivore.", "image_url": "https://via.placeholder.com/400x300?text=Kole"},
    {"id": 7, "common_name": "Moana Kali", "scientific_name": "Parupeneus cyclostomus", "sustainability_rating": "Sustainable", "health_notes": "Low mercury.", "preparation": "Steamed or fried.", "description": "Blue goatfish, culturally important in Hawaii.", "image_url": "https://via.placeholder.com/400x300?text=Moana_Kali"},
    {"id": 8, "common_name": "Ono", "scientific_name": "Acanthocybium solandri", "sustainability_rating": "Good Alternative", "health_notes": "Low to moderate mercury.", "preparation": "Grilled or sashimi.", "description": "Wahoo, a fast pelagic species popular in Hawaii.", "image_url": "https://via.placeholder.com/400x300?text=Ono"},
    {"id": 9, "common_name": "Opah", "scientific_name": "Lampris guttatus", "sustainability_rating": "Best Choice", "health_notes": "Low mercury.", "preparation": "Grilled or baked.", "description": "Moonfish, known for its round shaped body.", "image_url": "https://via.placeholder.com/400x300?text=Opah"},
    {"id": 10, "common_name": "Ta'ape", "scientific_name": "Lutjanus kasmira", "sustainability_rating": "Best Choice (Invasive)", "health_notes": "Low mercury.", "preparation": "Fried or grilled.", "description": "Bluestripe snapper - invasive species encouraged to harvest.", "image_url": "https://via.placeholder.com/400x300?text=Taape"},
    {"id": 11, "common_name": "Roi", "scientific_name": "Cephalopholis argus", "sustainability_rating": "Avoid (Invasive)", "health_notes": "High ciguatera risk.", "preparation": "Grilled or steamed.", "description": "Peacock grouper - invasive species, good to eat.", "image_url": "https://via.placeholder.com/400x300?text=Roi"},
    {"id": 12, "common_name": "Menpachi", "scientific_name": "Myripristis spp.", "sustainability_rating": "Sustainable", "health_notes": "Low mercury.", "preparation": "Fried.", "description": "Soldierfish, common in Hawaiian reefs.", "image_url": "https://via.placeholder.com/400x300?text=Menpachi"},
    {"id": 13, "common_name": "Kumu", "scientific_name": "Parupeneus porphyreus", "sustainability_rating": "Sustainable", "health_notes": "Low mercury.", "preparation": "Steamed.", "description": "Red goatfish, culturally significant in Hawaii.", "image_url": "https://via.placeholder.com/400x300?text=Kumu"},
    {"id": 14, "common_name": "Swordfish", "scientific_name": "Xiphias gladius", "sustainability_rating": "Good Alternative", "health_notes": "Higher mercury - limit intake.", "preparation": "Grilled steaks.", "description": "Broadbill swordfish caught by Hawaii longline.", "image_url": "https://via.placeholder.com/400x300?text=Swordfish"},
    {"id": 15, "common_name": "Bigeye Tuna", "scientific_name": "Thunnus obesus", "sustainability_rating": "Avoid / Caution", "health_notes": "Higher mercury levels.", "preparation": "Poke (limit portions).", "description": "Overfishing concerns in some Pacific stocks.", "image_url": "https://via.placeholder.com/400x300?text=Bigeye"},
    {"id": 16, "common_name": "Albacore", "scientific_name": "Thunnus alalunga", "sustainability_rating": "Good Alternative", "health_notes": "Low to moderate mercury.", "preparation": "Canned or fresh.", "description": "Caught by Hawaii troll fisheries.", "image_url": "https://via.placeholder.com/400x300?text=Albacore"},
    {"id": 17, "common_name": "He'e", "scientific_name": "Octopus cyanea", "sustainability_rating": "Sustainable", "health_notes": "Low mercury.", "preparation": "Poke, grilled.", "description": "Common octopus, important in traditional Hawaiian cuisine.", "image_url": "https://via.placeholder.com/400x300?text=Hee"},
    {"id": 18, "common_name": "Kona Crab", "scientific_name": "Ranina ranina", "sustainability_rating": "Sustainable", "health_notes": "Low mercury.", "preparation": "Steamed or boiled.", "description": "Regulated trap fishery in Hawaii.", "image_url": "https://via.placeholder.com/400x300?text=KonaCrab"},
    {"id": 19, "common_name": "Monchong", "scientific_name": "Taractichthys steindachneri", "sustainability_rating": "Good Alternative", "health_notes": "Low mercury.", "preparation": "Grilled or baked.", "description": "Pomfret caught as bycatch in longline fisheries.", "image_url": "https://via.placeholder.com/400x300?text=Monchong"},
    {"id": 20, "common_name": "Moi", "scientific_name": "Polydactylus sexfilis", "sustainability_rating": "Sustainable", "health_notes": "Low mercury.", "preparation": "Fried or steamed.", "description": "Threadfin, culturally important and stable population.", "image_url": "https://via.placeholder.com/400x300?text=Moi"},
]


@api_bp.route('/')
def home():
    return jsonify({"message": "Welcome to the Hawaii Seafood Guide", "description": "Helping consumers make informed and sustainable seafood choices in Hawaii", "models": {"fish_species": "/api/fish", "seafood_basics": "/api/basics", "consumer_guides": "/api/guides"}})

@api_bp.route('/api/fish', methods=['GET'])
def get_all_fish():
    search = request.args.get('search', '').lower()
    rating = request.args.get('rating')
    result = fish_species
    if search:
        result = [f for f in result if search in f['common_name'].lower() or search in f.get('hawaiian_name', '').lower()]
    if rating:
        result = [f for f in result if f['sustainability_rating'].lower() == rating.lower()]
    return jsonify(result)

@api_bp.route('/api/fish/<int:fish_id>', methods=['GET'])
def get_fish_by_id(fish_id):
    fish = next((f for f in fish_species if f['id'] == fish_id), None)
    if fish:
        return jsonify(fish)
    abort(404, description=f"Fish with id {fish_id} not found")

@api_bp.route('/api/guides', methods=['GET'])
def get_guides():
    guides = [{"id": 1, "title": "Best Fish for Poke", "summary": "Ahi, Tako, and He'e recommendations"}, {"id": 2, "title": "Low Mercury Options for Families", "summary": "Safe choices for children and pregnant women"}]
    return jsonify(guides)

@api_bp.errorhandler(404)
def not_found(error):
    return jsonify({"error": str(error.description)}), 404


# ── Overfished Areas (DJ) ─────────────────────────────────────────────────────

@api_bp.route('/api/overfished-areas', methods=['GET'])
def get_all_overfished_areas():
    status = request.args.get('status')
    query = OverfishedArea.query
    if status:
        query = query.filter(OverfishedArea.overfishing_status.ilike(f'%{status}%'))
    entries = query.order_by(OverfishedArea.area).all()
    return jsonify({"total": len(entries), "overfished_areas": [e.to_dict() for e in entries]}), 200

@api_bp.route('/api/overfished-areas/<int:entry_id>', methods=['GET'])
def get_overfished_area(entry_id):
    entry = db.session.get(OverfishedArea, entry_id)
    if not entry:
        return jsonify({"error": f"No overfished area found with id={entry_id}"}), 404
    return jsonify(entry.to_dict()), 200

@api_bp.route('/api/overfished-areas', methods=['POST'])
def create_overfished_area():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body must be JSON."}), 400
    missing = [f for f in ["area", "overfishing_status", "main_reasons"] if not data.get(f)]
    if missing:
        return jsonify({"error": f"Missing required fields: {missing}"}), 400
    entry = OverfishedArea(area=data["area"], overfishing_status=data["overfishing_status"], main_reasons=data["main_reasons"], source_link=data.get("source_link"))
    db.session.add(entry)
    db.session.commit()
    return jsonify(entry.to_dict()), 201

@api_bp.route('/api/overfished-areas/<int:entry_id>', methods=['DELETE'])
def delete_overfished_area(entry_id):
    entry = db.session.get(OverfishedArea, entry_id)
    if not entry:
        return jsonify({"error": f"No overfished area found with id={entry_id}"}), 404
    db.session.delete(entry)
    db.session.commit()
    return jsonify({"message": f"'{entry.area}' (id={entry_id}) deleted successfully."}), 200


# ── Imported Species (DJ) ─────────────────────────────────────────────────────

@api_bp.route('/api/imported-species', methods=['GET'])
def get_all_imported_species():
    volume = request.args.get('volume')
    query = ImportedSpecies.query
    if volume:
        query = query.filter(ImportedSpecies.annual_import_volume.ilike(f'%{volume}%'))
    entries = query.order_by(ImportedSpecies.species).all()
    return jsonify({"total": len(entries), "imported_species": [e.to_dict() for e in entries]}), 200

@api_bp.route('/api/imported-species/<int:entry_id>', methods=['GET'])
def get_imported_species(entry_id):
    entry = db.session.get(ImportedSpecies, entry_id)
    if not entry:
        return jsonify({"error": f"No imported species found with id={entry_id}"}), 404
    return jsonify(entry.to_dict()), 200

@api_bp.route('/api/imported-species', methods=['POST'])
def create_imported_species():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body must be JSON."}), 400
    missing = [f for f in ["species", "annual_import_volume", "main_reason"] if not data.get(f)]
    if missing:
        return jsonify({"error": f"Missing required fields: {missing}"}), 400
    entry = ImportedSpecies(species=data["species"], annual_import_volume=data["annual_import_volume"], main_reason=data["main_reason"], source_link=data.get("source_link"))
    db.session.add(entry)
    db.session.commit()
    return jsonify(entry.to_dict()), 201

@api_bp.route('/api/imported-species/<int:entry_id>', methods=['DELETE'])
def delete_imported_species(entry_id):
    entry = db.session.get(ImportedSpecies, entry_id)
    if not entry:
        return jsonify({"error": f"No imported species found with id={entry_id}"}), 404
    db.session.delete(entry)
    db.session.commit()
    return jsonify({"message": f"'{entry.species}' (id={entry_id}) deleted successfully."}), 200


# ── Fishing Methods (DJ) ──────────────────────────────────────────────────────

@api_bp.route('/api/fishing-methods', methods=['GET'])
def get_all_fishing_methods():
    rank = request.args.get('rank')
    query = FishingMethod.query
    if rank:
        query = query.filter(FishingMethod.sustainability_rank.ilike(f'%{rank}%'))
    entries = query.order_by(FishingMethod.method).all()
    return jsonify({"total": len(entries), "fishing_methods": [e.to_dict() for e in entries]}), 200

@api_bp.route('/api/fishing-methods/<int:entry_id>', methods=['GET'])
def get_fishing_method(entry_id):
    entry = db.session.get(FishingMethod, entry_id)
    if not entry:
        return jsonify({"error": f"No fishing method found with id={entry_id}"}), 404
    return jsonify(entry.to_dict()), 200

@api_bp.route('/api/fishing-methods', methods=['POST'])
def create_fishing_method():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body must be JSON."}), 400
    missing = [f for f in ["method", "description", "sustainability_rank", "key_reasons"] if not data.get(f)]
    if missing:
        return jsonify({"error": f"Missing required fields: {missing}"}), 400
    entry = FishingMethod(method=data["method"], description=data["description"], sustainability_rank=data["sustainability_rank"], key_reasons=data["key_reasons"], source_link=data.get("source_link"))
    db.session.add(entry)
    db.session.commit()
    return jsonify(entry.to_dict()), 201

@api_bp.route('/api/fishing-methods/<int:entry_id>', methods=['DELETE'])
def delete_fishing_method(entry_id):
    entry = db.session.get(FishingMethod, entry_id)
    if not entry:
        return jsonify({"error": f"No fishing method found with id={entry_id}"}), 404
    db.session.delete(entry)
    db.session.commit()
    return jsonify({"message": f"'{entry.method}' (id={entry_id}) deleted successfully."}), 200


# ── Consumer Guide (Kamryn) ──────────────────────────────────────────────────────

@api_bp.route('/api/consumer-guides', methods=['GET'])
def get_all_consumer_guides():
    filters = request.args.get('filters')
    query = ConsumerGuide.query
    if filters:
        query = query.filter(ConsumerGuide.filters.ilike(f'%{filters}%'))
    entries = query.order_by(ConsumerGuide.guide_name).all()
    return jsonify({"total": len(entries), "consumer_guides": [e.to_dict() for e in entries]}), 200

@api_bp.route('/api/consumer-guides/<int:entry_id>', methods=['GET'])
def get_consumer_guide(guide_id):
    entry = db.session.get(ConsumerGuide, guide_id)
    if not entry:
        return jsonify({"error": f"No guide found with id={entry_id}"}), 404
    return jsonify(entry.to_dict()), 200

@api_bp.route('/api/consumer-guides', methods=['POST'])
def create_consumer_guide():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body must be JSON."}), 400
    missing = [f for f in ["method", "description", "sustainability_rank", "key_reasons"] if not data.get(f)]
    if missing:
        return jsonify({"error": f"Missing required fields: {missing}"}), 400
    entry = ConsumerGuide(guide_name=data["guide_name"], description=data["description"], content=data["content"], filters=data["filters"], resources=data.get("resources"))
    db.session.add(entry)
    db.session.commit()
    return jsonify(entry.to_dict()), 201

@api_bp.route('/api/consumer-guides/<int:entry_id>', methods=['DELETE'])
def delete_consumer_guide(guide_id):
    entry = db.session.get(ConsumerGuide, guide_id)
    if not entry:
        return jsonify({"error": f"No guide found with id={entry_id}"}), 404
    db.session.delete(entry)
    db.session.commit()
    return jsonify({"message": f"'{entry.method}' (id={entry_id}) deleted successfully."}), 200