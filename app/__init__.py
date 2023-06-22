from flask import Flask
from .config import Config
from .api.user_routes import user_routes
from .api.auth_routes import auth_routes

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(user_routes, url_prefix='/api/users')
app.register_blueprint(auth_routes, url_prefix='/api/auth')
