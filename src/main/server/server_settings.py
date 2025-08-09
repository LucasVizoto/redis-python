from flask import Flask
from src.models.redis.settings.connection import redis_connection_handle
from src.models.sqlite.settings.connection import sqlite_connection_handler

from src.main.routes.products_routes import product_routes_bp

redis_connection_handle.connect()
sqlite_connection_handler.connect()

app = Flask(__name__)

app.register_blueprint(product_routes_bp)