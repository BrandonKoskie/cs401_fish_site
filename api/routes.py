from flask import Blueprint, jsonify, abort, request, render_template
from api.models import db
from api.models import OverfishedArea, ImportedSpecies, FishingMethod, ConsumerGuide

api_bp = Blueprint('api', __name__)

# ── Fish Species (Brandon's existing code) ────────────────────────────────────

@api_bp.route('/')
def home_page():
    return render_template('home.html')

@api_bp.route('/about')
def about_page():
    return render_template('about.html')

@api_bp.route('/guides')
def guides_page():
    return render_template('consumer_guides.html')

@api_bp.route('/basics')
def basics_page():
    return render_template('seafood_basics.html')

@api_bp.route('/fish')
def fish_page():
    return render_template('local_fish.html',)

fish_species = [
    {"id": 1, "common_name": "Ahi", "scientific_name": "Thunnus albacares", "sustainability_rating": "Good Alternative", "health_notes": "Moderate mercury levels. Pregnant women and children should limit intake.", "preparation": "Popular for poke, sashimi, and grilling.", "description": "Yellowfin tuna is one of the most important commercial fish in Hawaii.", "image_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.fishi-pedia.com%2Fwp-content%2Fuploads%2F2020%2F10%2FThunnus-albacares-725x483.jpg&f=1&nofb=1&ipt=b8522242eee1d1e2fb8919f4366ff0bd8f210d28d2e3984ec3a5f4a7747d718d"},
    {"id": 2, "common_name": "Mahimahi", "scientific_name": "Coryphaena hippurus", "sustainability_rating": "Best Choice", "health_notes": "Low mercury. High in protein and omega-3s.", "preparation": "Excellent for grilling, fish tacos, and ceviche.", "description": "Also known as dolphinfish, a fast-swimming pelagic species.", "image_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fchefsmandala.com%2Fwp-content%2Fuploads%2F2018%2F04%2FMahi-Mahi-Dolphin-Fish.jpg&f=1&nofb=1&ipt=0bebcac68e71c835847cbfd609227c613c1d14ef21137204ebaa38be73e869e9"},
    {"id": 3, "common_name": "Opakapaka", "scientific_name": "Pristipomoides filamentosus", "sustainability_rating": "Good Alternative", "health_notes": "Moderate mercury. Highly prized for fine dining.", "preparation": "Steamed or baked with ginger and green onions.", "description": "Pink snapper is a deep-water species valued for its delicate flavor.", "image_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.chefs-resources.com%2Fwp-content%2Fuploads%2FOpakapaka_2.jpg&f=1&nofb=1&ipt=39f83159da7a0642eaa153ca8e270391d9a69747ba431c70f0ef42eccee90d9d"},
    {"id": 4, "common_name": "Uku", "scientific_name": "Aprion virescens", "sustainability_rating": "Good Alternative", "health_notes": "Low to moderate mercury.", "preparation": "Fried or steamed.", "description": "Green jobfish, a common deep-water species in Hawaii.", "image_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.ytimg.com%2Fvi%2FaJjI48-4ylc%2Fmaxresdefault.jpg&f=1&nofb=1&ipt=66904e92a42ff821d6f6f539fcee5dab6cd11f9d124b3b9448fe2268a0935e52"},
    {"id": 5, "common_name": "Onaga", "scientific_name": "Etelis coruscans", "sustainability_rating": "Best Choice", "health_notes": "Low mercury. Popular in upscale restaurants.", "preparation": "Steamed or lightly seared.", "description": "Longtail snapper, prized for its firm white flesh.", "image_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.fisheries.noaa.gov%2Fs3%2Fstyles%2Ffull_width%2Fs3%2F2022-12%2Fsnapper-hires.jpg%3Fitok%3DptfSnffu&f=1&nofb=1&ipt=063873a3a0cb10cf4512d3a00c51ade757bd0825466274e67f84bec0e2e30df1"},
    {"id": 6, "common_name": "Kole", "scientific_name": "Ctenochaetus strigosus", "sustainability_rating": "Sustainable", "health_notes": "Low mercury.", "preparation": "Fried or grilled.", "description": "Goldring surgeonfish, a common reef herbivore.", "image_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.fishlaboratory.com%2Fwp-content%2Fuploads%2F2022%2F05%2FKole-Tang-2048x1357.jpeg&f=1&nofb=1&ipt=4e9173dff6af72ae34207e6394a07a4aa3703de69bb9e91c476a22c57ecebbbf"},
    {"id": 7, "common_name": "Moana Kali", "scientific_name": "Parupeneus cyclostomus", "sustainability_rating": "Sustainable", "health_notes": "Low mercury.", "preparation": "Steamed or fried.", "description": "Blue goatfish, culturally important in Hawaii.", "image_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.ytimg.com%2Fvi%2FJrgc4FATaEM%2Fmaxresdefault.jpg&f=1&nofb=1&ipt=bd2bb9bb2f3a7c86d0c43330235246fed2fc5917b13b83ddd469d1b9e5f3d55b"},
    {"id": 8, "common_name": "Ono", "scientific_name": "Acanthocybium solandri", "sustainability_rating": "Good Alternative", "health_notes": "Low to moderate mercury.", "preparation": "Grilled or sashimi.", "description": "Wahoo, a fast pelagic species popular in Hawaii.", "image_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwallpapers.com%2Fimages%2Fhd%2Fa-vibrant-wahoo-fish-swimming-underwater-in-its-natural-habitat-f52duh7frmr0al6j.jpg&f=1&nofb=1&ipt=f8991246070165b6c278477531c0b1f9881e409fd21164469efe140919190e43"},
    {"id": 9, "common_name": "Opah", "scientific_name": "Lampris guttatus", "sustainability_rating": "Best Choice", "health_notes": "Low mercury.", "preparation": "Grilled or baked.", "description": "Moonfish, known for its round shaped body.", "image_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Flecomptoirdelocean.pf%2Fwp-content%2Fuploads%2F2023%2F04%2Fmoonfish_comptoir.jpg&f=1&nofb=1&ipt=aa1f7e5408ad59e8d4d5c56113134ab3b5a2da8ed69645c3f81a21ae648081b5"},
    {"id": 10, "common_name": "Ta'ape", "scientific_name": "Lutjanus kasmira", "sustainability_rating": "Best Choice (Invasive)", "health_notes": "Low mercury.", "preparation": "Fried or grilled.", "description": "Bluestripe snapper - invasive species encouraged to harvest.", "image_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F2e%2Fac%2F0e%2F2eac0eed6f8fcb257b6e7a2e37cd58c8.jpg&f=1&nofb=1&ipt=210c912d8088339d534eee281afbd7a8b2197b7cf939807ad46fda04b04cfcb2"},
    {"id": 11, "common_name": "Roi", "scientific_name": "Cephalopholis argus", "sustainability_rating": "Avoid (Invasive)", "health_notes": "High ciguatera risk.", "preparation": "Grilled or steamed.", "description": "Peacock grouper - invasive species, good to eat.", "image_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fogden_images.s3.amazonaws.com%2Fwww.mauinews.com%2Fimages%2F2020%2F07%2F04041047%2F3-ROI.jpg&f=1&nofb=1&ipt=82250533d1e23064b5bdfd0bab7b0d5bde50d60569b032ee077b4b3543e8c200"},
    {"id": 12, "common_name": "Menpachi", "scientific_name": "Myripristis spp.", "sustainability_rating": "Sustainable", "health_notes": "Low mercury.", "preparation": "Fried.", "description": "Soldierfish, common in Hawaiian reefs.", "image_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%2Fid%2FOIP.MjVL_wMmt5K9NvV60irgewHaEK%3Fpid%3DApi&f=1&ipt=0e7363e0818e5146dbe1b49dea20fbccc3d6debd05ccf370ea8278717b6a8476&ipo=images"},
    {"id": 13, "common_name": "Kumu", "scientific_name": "Parupeneus porphyreus", "sustainability_rating": "Sustainable", "health_notes": "Low mercury.", "preparation": "Steamed.", "description": "Red goatfish, culturally significant in Hawaii.", "image_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2Foriginals%2Fb6%2Fea%2F8c%2Fb6ea8cd49e4d3b75202ab7f17327db07.jpg&f=1&nofb=1&ipt=00750d43861e8d1bda3dee9339fb16b92d5c20ccb6c9c4589e2883db07115a28"},
    {"id": 14, "common_name": "Swordfish", "scientific_name": "Xiphias gladius", "sustainability_rating": "Good Alternative", "health_notes": "Higher mercury - limit intake.", "preparation": "Grilled steaks.", "description": "Broadbill swordfish caught by Hawaii longline.", "image_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fadriaticnature.com%2Fwp-content%2Fuploads%2F2016%2F05%2FXiphias-gladius-2.jpg&f=1&nofb=1&ipt=0eaa5093810119d466991a8417aeb6ae7d49d657fbcc4129dca953f4ced020fe"},
    {"id": 15, "common_name": "Bigeye Tuna", "scientific_name": "Thunnus obesus", "sustainability_rating": "Avoid / Caution", "health_notes": "Higher mercury levels.", "preparation": "Poke (limit portions).", "description": "Overfishing concerns in some Pacific stocks.", "image_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn2.webdamdb.com%2F1280_Iro3MCOE8Ji4.jpg%3F1597172104&f=1&nofb=1&ipt=bc631a47f4bf13456aa589580f70a908b002061d2bdf3f670d29d16351e6f3b3"},
    {"id": 16, "common_name": "Albacore", "scientific_name": "Thunnus alalunga", "sustainability_rating": "Good Alternative", "health_notes": "Low to moderate mercury.", "preparation": "Canned or fresh.", "description": "Caught by Hawaii troll fisheries.", "image_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fa-z-animals.com%2Fmedia%2F2021%2F01%2FTuna-Albacore-swimming.jpg&f=1&nofb=1&ipt=65bb2b2f5dcf999f7a33e11388d39969f7f219a38116e45d4253772126ba6886"},
    {"id": 17, "common_name": "He'e", "scientific_name": "Octopus cyanea", "sustainability_rating": "Sustainable", "health_notes": "Low mercury.", "preparation": "Poke, grilled.", "description": "Common octopus, important in traditional Hawaiian cuisine.", "image_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.natgeofe.com%2Fk%2Fdd877026-79be-4a9c-ad57-e9250308eb83%2Foctopus-ocean-floor_3x2.jpg&f=1&nofb=1&ipt=b2b4863ddac1550103e318737e27a45be84c1fa2b4c7209e422be62e8d8bdf6d"},
    {"id": 18, "common_name": "Kona Crab", "scientific_name": "Ranina ranina", "sustainability_rating": "Sustainable", "health_notes": "Low mercury.", "preparation": "Steamed or boiled.", "description": "Regulated trap fishery in Hawaii.", "image_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.e-fish.com%2Fcdn%2Fshop%2Ffiles%2FIMG_7779_1024x.jpg%3Fv%3D1729263803&f=1&nofb=1&ipt=b49bfaf8050df7def5fdeabc5971ca32198dfd29324115da1132f5eae3c1ed68"},
    {"id": 19, "common_name": "Monchong", "scientific_name": "Taractichthys steindachneri", "sustainability_rating": "Good Alternative", "health_notes": "Low mercury.", "preparation": "Grilled or baked.", "description": "Pomfret caught as bycatch in longline fisheries.", "image_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fhawaiianseafood.com%2Fwp-content%2Fuploads%2F2025%2F03%2FHawaiian-Seafood-Hawaii-Monchong-fish-1000sq.jpg&f=1&nofb=1&ipt=b3dbd1ec69655fb3f9c7fa9211b7b9109d7bfe02e1398ff6e2d2102af722a270"},
    {"id": 20, "common_name": "Moi", "scientific_name": "Polydactylus sexfilis", "sustainability_rating": "Sustainable", "health_notes": "Low mercury.", "preparation": "Fried or steamed.", "description": "Threadfin, culturally important and stable population.", "image_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2F736x%2F16%2F2a%2F79%2F162a79c87848bd575af950b0d31a1dd9.jpg&f=1&nofb=1&ipt=ffdb8928fba774e50f7aedced604af55a4bbb7d3040aeade925c0673256f9726"},
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

CONSUMER_GUIDES = [
    {"guide_name": "Top Sustainable Poke Fish", "description": "Find enviornmentally friendly fish commonly used in poke bowls", "content": "Recommended species: Ahi, Salmon. Tip: Choose locally caught fish to reduce environmental impact. Recipe idea: Build a poke bowl with rice as a base, add cubed salmon or tuna, and optional toppings like seaweed, cucumber, and furikake for extra flavor.","filters": "poke, ahi, popular",
        "resources": " NOAA Sustainable Seafood"},
    {"guide_name": "Low Mercury Options for Families", "description": "Provides safe seafood choices for children and pregnant women.", "content": "Recommended species: Salmon (Low mercury), Sardines (Low mercury), Shrimp (Very low mercury), Tilapia. Tip: To avoid high-mercury fish like swordfish and bigeye tuna. Recipe idea: Grilled salmon with lemon.", "filters": "low mercury, health", "resources": "FDA Seafood Consumption"},
    {"guide_name": "Budget Friendly Healthy Seafood Options", "description": "Affordable seafood options that are healthy and widely available.", "content": "Recommended species: Canned light tuna, Sardines, Pollock. Tip: Frozen and canned options are often cheaper but still nutritious. Recipe idea: Tuna sandwich - add mayonnaise and chopped celery to canned tuna.", "filters": "budget, low cost, easy meals", "resources": "USDA Seafood Nutrition"},
    {"guide_name": "Seasonal Seafood Guide", "description": "Shows the best seasonal seafood options to support sustainable fishing.", "content": "Recommended seasonal fish: Ahi (year around), Mahi Mahi (spring and summer), Shrimp (year around). Tip: Eating in-season seafood reduces pressure on fish populations. Recipe idea: Seafood and white rice", "filters": "seasonal, fish, sustainable", "resources": "Hawaii Division of Aquatic Resources"},
    {"guide_name": "Beginner’s Guide to Sustainable Seafood", "description": "Introduces beginners to making seafood choices.", "content": "Recommended species: Salmon, Tuna, Shrimp. Tip: Look for seafood certified by sustainability programs. Recipe idea: Simple baked salmon with vegetables.", "filters": "beginner, sustainable, easy", "resources": "Seafood Watch Beginner Guide"},
    {"guide_name": "Healthy Grilling & Cooking Seafood Guide", "description": "Healthy cooking methods for seafood and seafood preparation techniques.", "content": "Recommended species: Salmon, Mahi-Mahi, Shrimp. Tip: Grilling and baking preserve nutrients and reduce added fats. Recipe idea: Grilled mahi-mahi tacos with cabbage slaw.", "filters": "cooked, grilling, recipes", "resources": "NOAA Cooking Guide"}
]

@api_bp.route('/api/consumer-guides', methods=['GET'])
def get_all_consumer_guides():
    filters = request.args.get('filters', '').lower()

    result = CONSUMER_GUIDES  

    if filters:
        result = [
            g for g in result
            if filters in g.get("filters", "").lower()
        ]

    return jsonify(result)


@api_bp.route('/api/consumer-guides/<int:guide_id>', methods=['GET'])
def get_consumer_guide(guide_id):
    guide = next((g for g in CONSUMER_GUIDES if g.get("id") == guide_id), None)

    if not guide:
        return jsonify({"error": f"No guide found with id={guide_id}"}), 404

    return jsonify(guide), 200

@api_bp.route('/api/consumer-guides', methods=['POST'])
def create_consumer_guide():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    required_fields = ["guide_name", "description", "content", "filters"]

    missing = [f for f in required_fields if not data.get(f)]
    if missing:
        return jsonify({"error": f"Missing fields: {missing}"}), 400

    # auto-generate ID
    new_id = max([g.get("id", 0) for g in CONSUMER_GUIDES], default=0) + 1
    data["id"] = new_id

    CONSUMER_GUIDES.append(data)

    return jsonify(data), 201

@api_bp.route('/api/consumer-guides/<int:guide_id>', methods=['DELETE'])
def delete_consumer_guide(guide_id):
    global CONSUMER_GUIDES

    original_length = len(CONSUMER_GUIDES)

    CONSUMER_GUIDES = [
        g for g in CONSUMER_GUIDES if g.get("id") != guide_id
    ]

    if len(CONSUMER_GUIDES) == original_length:
        return jsonify({"error": f"No guide found with id={guide_id}"}), 404

    return jsonify({"message": f"Guide {guide_id} deleted"}), 200 