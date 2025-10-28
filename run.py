from app import create_app
from app.extensions import db

app = create_app()

if __name__ == '__main__':
    with app.app_context():

        try:
            db.engine.connect()
            print("✅ DB connection OK!")
            
        except Exception as e:
            print("❌ DB connection failed:", e)
        # db.drop_all()
        db.create_all()

    app.run(debug=True)