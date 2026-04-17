from flask import Blueprint, jsonify, abort, request, render_template

api_bp = Blueprint('api', __name__)

# Route for the fish species html page
@api_bp.route('/fish')
def fish_page():
    return render_template('local_fish.html')

# FishSpecies Model - now includes sustainability rating directly
fish_species = [    
    {
        "id": 1,
        "common_name": "Ahi",
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
        "scientific_name": "Coryphaena hippurus",
        "sustainability_rating": "Best Choice",
        "health_notes": "Low mercury. High in protein and omega-3s.",
        "preparation": "Excellent for grilling, fish tacos, and ceviche.",
        "description": "Also known as dolphinfish, a fast-swimming pelagic species.",
        "image_url": "https://via.placeholder.com/400x300?text=Mahimahi"
    },
    {
        "id": 3,
        "common_name": "Opakapaka",
        "scientific_name": "Pristipomoides filamentosus",
        "sustainability_rating": "Good Alternative",
        "health_notes": "Moderate mercury. Highly prized for fine dining.",
        "preparation": "Steamed or baked with ginger and green onions.",
        "description": "Pink snapper is a deep-water species valued for its delicate flavor.",
        "image_url": "https://via.placeholder.com/400x300?text=Opakapaka"
    },
    {
        "id": 4,
        "common_name": "Uku",
        "scientific_name": "Aprion virescens",
        "sustainability_rating": "Good Alternative",
        "health_notes": "Low to moderate mercury.",
        "preparation": "Fried or steamed.",
        "description": "Green jobfish, a common deep-water species in Hawaii.",
        "image_url": "https://via.placeholder.com/400x300?text=Uku"
    },
    {
        "id": 5,
        "common_name": "Onaga",
        "scientific_name": "Etelis coruscans",
        "sustainability_rating": "Best Choice",
        "health_notes": "Low mercury. Popular in upscale restaurants.",
        "preparation": "Steamed or lightly seared.",
        "description": "Longtail snapper, prized for its firm white flesh.",
        "image_url": "https://via.placeholder.com/400x300?text=Onaga"
    },
    {
        "id": 6,
        "common_name": "Kole",
        "scientific_name": "Ctenochaetus strigosus",
        "sustainability_rating": "Sustainable",
        "health_notes": "Low mercury.",
        "preparation": "Fried or grilled.",
        "description": "Goldring surgeonfish, a common reef herbivore.",
        "image_url": "https://via.placeholder.com/400x300?text=Kole"
    },
    {
        "id": 7,
        "common_name": "Moana Kali",
        "scientific_name": "Parupeneus cyclostomus",
        "sustainability_rating": "Sustainable",
        "health_notes": "Low mercury.",
        "preparation": "Steamed or fried.",
        "description": "Blue goatfish, culturally important in Hawaii.",
        "image_url": "https://via.placeholder.com/400x300?text=Moana_Kali"
    },
    {
        "id": 8,
        "common_name": "Ono",
        "scientific_name": "Acanthocybium solandri",
        "sustainability_rating": "Good Alternative",
        "health_notes": "Low to moderate mercury.",
        "preparation": "Grilled or sashimi.",
        "description": "Wahoo, a fast pelagic species popular in Hawaii.",
        "image_url": "https://via.placeholder.com/400x300?text=Ono"
    },
    {
        "id": 9,
        "common_name": "Opah",
        "scientific_name": "Lampris guttatus",
        "sustainability_rating": "Best Choice",
        "health_notes": "Low mercury.",
        "preparation": "Grilled or baked.",
        "description": "Moonfish, known for its round shaped body.",
        "image_url": "https://via.placeholder.com/400x300?text=Opah"
    },
    {
        "id": 10,
        "common_name": "Taʻape",
        "scientific_name": "Lutjanus kasmira",
        "sustainability_rating": "Best Choice (Invasive)",
        "health_notes": "Low mercury.",
        "preparation": "Fried or grilled.",
        "description": "Bluestripe snapper – invasive species encouraged to harvest.",
        "image_url": "https://via.placeholder.com/400x300?text=Taape"
    },
    {
        "id": 11,
        "common_name": "Roi",
        "scientific_name": "Cephalopholis argus",
        "sustainability_rating": "Avoid (Invasive)",
        "health_notes": "High ciguatera risk.",
        "preparation": "Grilled or steamed.",
        "description": "Peacock grouper – invasive species, good to eat.",
        "image_url": "https://via.placeholder.com/400x300?text=Roi"
    },
    {
        "id": 12,
        "common_name": "Menpachi",
        "scientific_name": "Myripristis spp.",
        "sustainability_rating": "Sustainable",
        "health_notes": "Low mercury.",
        "preparation": "Fried.",
        "description": "Soldierfish, common in Hawaiian reefs.",
        "image_url": "https://via.placeholder.com/400x300?text=Menpachi"
    },
    {
        "id": 13,
        "common_name": "Kumu",
        "scientific_name": "Parupeneus porphyreus",
        "sustainability_rating": "Sustainable",
        "health_notes": "Low mercury.",
        "preparation": "Steamed.",
        "description": "Red goatfish, culturally significant in Hawaii.",
        "image_url": "https://via.placeholder.com/400x300?text=Kumu"
    },
    {
        "id": 14,
        "common_name": "Swordfish",
        "scientific_name": "Xiphias gladius",
        "sustainability_rating": "Good Alternative",
        "health_notes": "Higher mercury – limit intake.",
        "preparation": "Grilled steaks.",
        "description": "Broadbill swordfish caught by Hawaii longline.",
        "image_url": "https://via.placeholder.com/400x300?text=Swordfish"
    },
    {
        "id": 15,
        "common_name": "Bigeye Tuna",
        "scientific_name": "Thunnus obesus",
        "sustainability_rating": "Avoid / Caution",
        "health_notes": "Higher mercury levels.",
        "preparation": "Poke (limit portions).",
        "description": "Overfishing concerns in some Pacific stocks.",
        "image_url": "https://via.placeholder.com/400x300?text=Bigeye"
    },
    {
        "id": 16,
        "common_name": "Albacore",
        "scientific_name": "Thunnus alalunga",
        "sustainability_rating": "Good Alternative",
        "health_notes": "Low to moderate mercury.",
        "preparation": "Canned or fresh.",
        "description": "Caught by Hawaii troll fisheries.",
        "image_url": "https://via.placeholder.com/400x300?text=Albacore"
    },
    {
        "id": 17,
        "common_name": "Heʻe",
        "scientific_name": "Octopus cyanea",
        "sustainability_rating": "Sustainable",
        "health_notes": "Low mercury.",
        "preparation": "Luau, poke, grilled.",
        "description": "Common octopus, important in traditional Hawaiian cuisine.",
        "image_url": "https://via.placeholder.com/400x300?text=Hee"
    },
    {
        "id": 18,
        "common_name": "Kona Crab",
        "scientific_name": "Ranina ranina",
        "sustainability_rating": "Sustainable",
        "health_notes": "Low mercury.",
        "preparation": "Steamed or boiled.",
        "description": "Regulated trap fishery in Hawaii.",
        "image_url": "https://via.placeholder.com/400x300?text=KonaCrab"
    },
    {
        "id": 19,
        "common_name": "Monchong",
        "scientific_name": "Taractichthys steindachneri",
        "sustainability_rating": "Good Alternative",
        "health_notes": "Low mercury.",
        "preparation": "Grilled or baked.",
        "description": "Pomfret caught as bycatch in longline fisheries.",
        "image_url": "https://via.placeholder.com/400x300?text=Monchong"
    },
    {
        "id": 20,
        "common_name": "Moi",
        "scientific_name": "Polydactylus sexfilis",
        "sustainability_rating": "Sustainable",
        "health_notes": "Low mercury.",
        "preparation": "Fried or steamed.",
        "description": "Threadfin, culturally important and stable population.",
        "image_url": "https://via.placeholder.com/400x300?text=Moi"
    }
]

@api_bp.route('/')
def home():
    return jsonify({
        "message": "Welcome to Sustainable Hawaii Seafood Guide",
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
