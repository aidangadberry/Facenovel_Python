from flask_login import UserMixin
import bcrypt
from .db import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    fname = db.Column(db.String(255))
    lname = db.Column(db.String(255))
    birthday = db.Column(db.Date())

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        salt = bcrypt.gensalt()
        self.hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.hashed_password)
