from flask import Flask
from api.routes import api_bp   # we'll create routes.py next

app = Flask(__name__)

# Register blueprint for routes
app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)