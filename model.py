import email
from sqlite3 import connect
from unicodedata import name
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import PrimaryKeyConstraint
from flask_debugtoolbar import DebugToolbarExtension
# from server import app

db = SQLAlchemy()

# from app import db, create_app
# app = create_app()
# app.app_context().push()


def create_app():
    app = Flask(__name__)
    db.init_app(app)
    return app


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(80), unique=True)
    
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Sits(db.Model):

    __tablename__ = "sits"

    id = db.Column(db.Integer, primary_key=True)
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

    def __init__(self, name, address, phone_number, email, avg_bill, total_kwh, new_price_with, new_price_without, offset, panels, notes):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.avg_bill = avg_bill
        self.total_kwh = total_kwh
        self.new_price_with = new_price_with
        self.new_price_without = new_price_without
        self.offset = offset
        self.panels = panels
        self.notes = notes


class Sold(db.Model):

    __tablename__ = "sold"

    id = db.Column(db.Integer, primary_key=True)
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

    def __init__(self, name, address, phone_number, email, avg_bill, total_kwh, new_price_with, new_price_without, offset, panels, loan_provider, interest_rate, date_sold, notes):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.avg_bill = avg_bill
        self.total_kwh = total_kwh
        self.new_price_with = new_price_with
        self.new_price_without = new_price_without
        self.offset = offset
        self.panels = panels
        self.loan_provider = loan_provider
        self.interest_rate = interest_rate
        self.date_sold = date_sold
        self.notes = notes


def connect_to_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://Jaxson:sqlpassword@localhost:5432/capstone-final'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    app = Flask(__name__)
    connect_to_db(app)
    db.create_all()
    print("Connected to database")
