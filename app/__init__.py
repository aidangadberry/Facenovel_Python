from flask import Flask
from sqlalchemy.sql import text
from .config import Config
from .api.user_routes import user_routes
from .api.auth_routes import auth_routes
from .models import db

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(user_routes, url_prefix='/api/users')
app.register_blueprint(auth_routes, url_prefix='/api/auth')
db.init_app(app)


@app.route('/')
def index():
    try:
        db.session.query(text("1")).from_statement(text("SELECT 1")).all()
        return f"<h1>It works!</h1>"
    except Exception as ex:
        return f"<h1>Something is broken: {ex}</h1>"
