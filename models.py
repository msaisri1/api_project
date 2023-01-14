from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    createdAt = db.Column(db.String(100))
    name = db.Column(db.String(100))
    avatar = db.Column(db.String(200))
    payments = db.Column(db.String(200))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))