from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from datetime import datetime
#from flask import Flask
#from models import db

db = SQLAlchemy()


def init_app(application):
    db.app = application
    db.init_app(application)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    is_admin = db.Column(db.Boolean)
    api_key = db.Column(db.String(255), unique=True, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    authenticated = db.Column(db.Boolean, default=False)
    role=db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __repr__(self):
        return f'<user {self.id}, {self.username}>'

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'is_admin': self.is_admin,
            'api_key': self.api_key,
            'is_active': self.is_active,
            'email':self.email,
            'role':self.role,
        }

    def update_api_key(self):
        self.api_key = generate_password_hash(self.username + str(datetime.utcnow))
