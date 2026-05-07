import os
from flask import Flask
from api.models import db

def create_app():
    app = Flask(__name__,
                static_folder='../static',      
                static_url_path='/static')      

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hawaii_seafood.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from api.models import OverfishedArea, ImportedSpecies, FishingMethod # noqa
    from api.routes import api_bp
    app.register_blueprint(api_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
