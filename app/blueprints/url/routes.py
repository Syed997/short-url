from flask import Blueprint, request, jsonify
from app.models.url_model import URL
from app.extensions import db


url_bp = Blueprint('url_bp', __name__)


@url_bp.route('/add', methods=['POST'])
def url_shorter():
    data=request.get_json()

    url = data.get('url')
    short_url = data.get('short_url')

    if not url or not short_url:
        return jsonify({"error": "url and short url are required!"}), 400
    
    new_url = URL(url=url , short_url=short_url)
    db.session.add(new_url)
    db.session.commit()
    return jsonify({"message":"short url added successfully", "id": new_url.id}), 201

@url_bp.route('/list')
def get_url():
    urls = URL.query.all()
    results = [{"id":u.id, "url": u.url, "short_url": u.short_url }for u in urls]
    return jsonify(results), 200