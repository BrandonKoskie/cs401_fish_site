from flask import Blueprint, jsonify, abort, request

api_bp = Blueprint('api', __name__)

# FishSpecies Model - now includes sustainability rating directly
fish_species = [
    {
        "id": 1,
        "common_name": "Ahi",
        "hawaiian_name": "ʻAhi",
        "scientific_name": "Thunnus albacares",
        "sustainability_rating": "Good Alternative",
        "health_notes": "Moderate mercury levels. Pregnant women and children should limit intake.",
        "preparation": "Popular for poke, sashimi, and grilling.",
        "description": "Yellowfin tuna is one of the most important commercial fish in Hawaii.",
        "image_url": "https://via.placeholder.com/400x300?text=Ahi"
    },
    {
        "id": 2,
        "common_name": "Mahimahi",
        "hawaiian_name": "Mahimahi",
        "scientific_name": "Coryphaena hippurus",
        "sustainability_rating": "Best Choice",
        "health_notes": "Low mercury. High in protein and omega-3 fatty acids.",
        "preparation": "Excellent for grilling, fish tacos, and ceviche.",
        "description": "Also known as dolphinfish, mahimahi is a fast-swimming pelagic species.",
        "image_url": "https://via.placeholder.com/400x300?text=Mahimahi"
    },
    {
        "id": 3,
        "common_name": "Opakapaka",
        "hawaiian_name": "ʻOpakapaka",
        "scientific_name": "Pristipomoides filamentosus",
        "sustainability_rating": "Good Alternative",
        "health_notes": "Moderate mercury. Highly valued in Hawaiian fine dining.",
        "preparation": "Often steamed with ginger and green onions.",
        "description": "Pink snapper is a deep-water species prized for its delicate flavor.",
        "image_url": "https://via.placeholder.com/400x300?text=Opakapaka"
    }
]

@api_bp.route('/')
def home():
    return jsonify({
        "message": "Welcome to Sustainable Hawaiian Seafood Guide",
        "description": "Helping consumers make informed and sustainable seafood choices in Hawaii",
        "models": {
            "fish_species": "/api/fish",
            "seafood_basics": "/api/basics",
            "consumer_guides": "/api/guides"
        }
    })

@api_bp.route('/api/fish', methods=['GET'])
def get_all_fish():
    search = request.args.get('search', '').lower()
    rating = request.args.get('rating')

    result = fish_species

    if search:
        result = [f for f in result if search in f['common_name'].lower() or 
                                      search in f.get('hawaiian_name', '').lower()]

    if rating:
        result = [f for f in result if f['sustainability_rating'].lower() == rating.lower()]

    return jsonify(result)

@api_bp.route('/api/fish/<int:fish_id>', methods=['GET'])
def get_fish_by_id(fish_id):
    fish = next((f for f in fish_species if f['id'] == fish_id), None)
    if fish:
        return jsonify(fish)
    abort(404, description=f"Fish with id {fish_id} not found")

# Placeholder for Hawaii Seafood Basics (we'll expand this soon)
@api_bp.route('/api/basics', methods=['GET'])
def get_seafood_basics():
    basics = {
        "title": "Hawaii Seafood Basics",
        "overview": "Hawaii's ocean provides over 50% of the seafood consumed locally.",
        "challenges": ["Overfishing", "Climate change", "Coral bleaching", "Pollution"],
        "cultural_importance": "Seafood is central to Hawaiian culture, from traditional poke to modern cuisine.",
        "key_fact": "The state has strict fishing regulations to protect reef fish and pelagic species."
    }
    return jsonify(basics)

# Placeholder for Consumer Guides
@api_bp.route('/api/guides', methods=['GET'])
def get_guides():
    guides = [
        {"id": 1, "title": "Best Fish for Poke", "summary": "Ahi, Tako, and He'e recommendations"},
        {"id": 2, "title": "Low Mercury Options for Families", "summary": "Safe choices for children and pregnant women"}
    ]
    return jsonify(guides)

@api_bp.errorhandler(404)
def not_found(error):
    return jsonify({"error": str(error.description)}), 404