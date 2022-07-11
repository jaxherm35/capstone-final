import email
from unicodedata import name
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Sits(db.Model):

    __tablename__ = "sits"

    name = db.Column(db.String(80))
    address = db.Column(db.String(80))
    phone_number = db.Column(db.String(80), nullable=True)
    email = db.Column(db.String(80), nullable=True)
    avg_bill = db.Column(db.String(80))
    total_kwh = db.Column(db.Integer())
    new_price_with = db.Column(db.Integer())
    new_price_without = db.Column(db.Integer())
    offset = db.Column(db.Integer())
    panels = db.Column(db.Integer())

