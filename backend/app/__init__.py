# backend/app/__init__.py
from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    # Mengaktifkan CORS untuk semua rute dan origin tertentu (misalnya, http://localhost:3000)
    CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
    # Menambahkan rute dan komponen lainnya
    from .routes import bp
    app.register_blueprint(bp)
    return app