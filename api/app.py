import os
from flask import Flask
from api.models import db

def create_app():
    # Use absolute path to database
    basedir = os.path.abspath(os.path.dirname(__file__))
    instance_path = os.path.join(os.path.dirname(basedir), 'instance')
    db_path = os.path.join(instance_path, 'hawaii_seafood.db')
    
    app = Flask(__name__,
                static_folder='../static',      
                static_url_path='/static')      

    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["INSTANCE_PATH"] = instance_path

    db.init_app(app)

    from api.models import OverfishedArea, ImportedSpecies, FishingMethod # noqa
    from api.routes import api_bp
    app.register_blueprint(api_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
