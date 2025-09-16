from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Predefined disaster responses with extra details
responses = {
    "earthquake": {
        "message": "Drop, Cover, and Hold! Stay away from windows and heavy objects.",
        "emergency_numbers": ["100", "101", "108"],
        "safe_zones": ["City Stadium", "Community Hall A"],
        "maps_link": "https://maps.google.com/?q=earthquake+shelter"
    },
    "fire": {
        "message": "Stay low, cover your nose with cloth, and exit through the nearest safe route.",
        "emergency_numbers": ["101", "112"],
        "safe_zones": ["Central School Ground", "Fire Assembly Point"],
        "maps_link": "https://maps.google.com/?q=fire+assembly+point"
    },
    "flood": {
        "message": "Move to higher ground immediately. Avoid walking through moving water.",
        "emergency_numbers": ["108", "112"],
        "safe_zones": ["Community Hall B", "High School Building"],
        "maps_link": "https://maps.google.com/?q=flood+shelter"
    },
    "cyclone": {
        "message": "Stay indoors, away from windows. Keep emergency supplies handy.",
        "emergency_numbers": ["100", "108"],
        "safe_zones": ["Cyclone Shelter A", "Relief Camp B"],
        "maps_link": "https://maps.google.com/?q=cyclone+shelter"
    }
}

# Root route
@app.route("/")
def home():
    return "🌐 Disaster API is running! Use GET /flood or POST /disaster with JSON {'disaster': 'fire'}"

# GET method (via URL parameter)
@app.route("/<disaster>", methods=["GET"])
def disaster_get(disaster):
    details = responses.get(disaster.lower())
    if not details:
        return jsonify({"error": "No information available for this disaster."}), 404
    
    details["timestamp"] = datetime.utcnow().isoformat()
    return jsonify({"disaster": disaster, **details})

# POST method (via JSON body)
@app.route("/disaster", methods=["POST"])
def disaster_post():
    data = request.get_json()
    if not data or "disaster" not in data:
        return jsonify({"error": "Please provide a disaster in JSON format. Example: {'disaster': 'fire'}"}), 400
    
    disaster = data["disaster"].lower()
    details = responses.get(disaster)
    if not details:
        return jsonify({"error": "No information available for this disaster."}), 404
    
    details["timestamp"] = datetime.utcnow().isoformat()
    return jsonify({"disaster": disaster, **details})


if __name__ == "__main__":
    app.run(debug=True)
