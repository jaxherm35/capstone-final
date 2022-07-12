import email
from sqlite3 import connect
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
    notes = db.Column(db.String(300))

class Sold(db.Model):

    __tablename__ = "sold"

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
    loan_provider = db.Column(db.String(80))
    interest_rate = db.Column(db.String(20))
    date_sold = db.Column(db.String(20))
    notes = db.Column(db.String(300))


def connect_to_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://Jaxson:sqlpassword@localhost:5432/capstone-final'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app= app
    db.init_app(app)


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    print("Connected to database")

