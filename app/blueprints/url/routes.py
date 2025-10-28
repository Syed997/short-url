from flask import Blueprint, request, jsonify
from app.models.url_model import URL
from app.extensions import db
from app.utils.services import add_url, get_actual_url


url_bp = Blueprint('url_bp', __name__)


@url_bp.route('/add', methods=['POST'])
def url_shorter():
    data=request.get_json()

    url = data.get('url')
    short_url = data.get('short_url')

    if not url or not short_url:
        return jsonify({"error": "url and short url are required!"}), 400
    
    # new_url = URL(url=url , short_url=short_url)
    # db.session.add(new_url)
    # db.session.commit()
    # return jsonify({"message":"short url added successfully", "id": new_url.id}), 201
    id = add_url(url, short_url)

    if not id:
        return jsonify({"error": "database operation failed"}), 400
    
    return jsonify({"message": "succesfull", "id": id})



@url_bp.route('/list')
def get_url():
    urls = URL.query.all()
    results = [{"id":u.id, "url": u.url, "short_url": u.short_url }for u in urls]
    return jsonify(results), 200


@url_bp.route('/<string:short_url>')
def redirect(short_url):
    url = get_actual_url(short_url)

    if not url:
        return jsonify({"message": "no data found"}), 200
    
    return jsonify({"url": url}), 200
