from flask import Flask, request, jsonify
from flask_cors import CORS
from route_model import get_safe_route

app = Flask(__name__)
CORS(app)

@app.route("/route", methods=["POST"])
def route():
    data = request.json
    source = data["source"]
    destination = data["destination"]

    try:
        path = get_safe_route(source, destination)
        return jsonify({"route": path})
    except:
        return jsonify({"error": "Route not found"}), 400

if __name__ == "__main__":
    app.run(debug=True)
