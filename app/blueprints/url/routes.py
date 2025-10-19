from flask import Blueprint, request, jsonify


url_bp = Blueprint('url_bp', __name__)


@url_bp.route('/shorter', methods=['POST'])
def url_shorter():
    data = request.get_json()

    if not data:
        return jsonify({"error": "no data found."}), 400
    
    url = data.get("url")
    short_url = data.get("short_url")

    return jsonify({
        "message": "data received.",
        "data": {
            "short_url" : short_url
        }
    })