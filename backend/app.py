from flask import Flask, request, jsonify
from flask_cors import CORS
from model import recommend

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend integration

@app.route("/recommend", methods=["GET"])
def get_recommendations():
    city = request.args.get("city")
    
    if not city:
        return jsonify({"error": "City parameter is required"}), 400

    recommendations = recommend(city)

    if not recommendations:
        return jsonify({"error": "City not found"}), 404

    return jsonify({"city": city, "recommendations": recommendations})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
