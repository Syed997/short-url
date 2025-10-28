from app.models.url_model import URL
from app.extensions import db

def add_url(url, short_url):
    new_url = URL(url=url, short_url=short_url)
    db.session.add(new_url)
    db.session.commit()

    return new_url.id

def get_actual_url(short_url):
    url = URL.query.filter_by(short_url=short_url).first()
    # print(url.url)
    
    return url.url