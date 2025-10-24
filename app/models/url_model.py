from app.extensions import db

class URL(db.Model):
    __tablename__ = 'urls'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200), nullable=False)
    short_url = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"<URL {self.name}>"