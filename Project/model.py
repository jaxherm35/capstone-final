# from ast import For
# from audioop import avg
# from ctypes import addressof
# import email
# from hashlib import new
# from sqlite3 import connect
# from unicodedata import name
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import PrimaryKeyConstraint, ForeignKey
from flask_debugtoolbar import DebugToolbarExtension
from Project import db

class User(db.Model):

    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
   
    
    def __init__(self, name):
        self.name = name


class Homeowner(db.Model):

    __tablename__ = 'homeowner'

    homeowner_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    address = db.Column(db.String(80))
    phone_number = db.Column(db.String(80))
    email = db.Column(db.String(80))
    avg_bill = db.Column(db.String(80))
    total_kwh = db.Column(db.String(80))

    def __init__(self, homeowner_id, name, phone_number, email, avg_bill, total_kwh):
        self.homeowner_id = homeowner_id
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.avg_bill = avg_bill
        self.total_kwh = total_kwh


class Sits(db.Model):

    __tablename__ = "sits"

    sit_id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), ForeignKey("user.user_id"))
    homeowner_id = db.Column(db.Integer(), ForeignKey("homeowner.homeowner_id"))
    new_price_with = db.Column(db.Integer())
    new_price_without = db.Column(db.Integer())
    offset = db.Column(db.Integer())
    panels = db.Column(db.Integer())
    notes = db.Column(db.String(300))



    def __init__(self, sit_id, new_price_with, new_price_without, offset, panels, notes):
        self.sit_id = sit_id
        self.new_price_with = new_price_with
        self.new_price_without = new_price_without
        self.offset = offset
        self.panels = panels
        self.notes = notes



class Sold(db.Model):

    __tablename__ = "sold"

    sold_id = db.Column(db.Integer(), primary_key=True)
    sit_id = db.Column(db.Integer(), ForeignKey("sits.sit_id"))
    new_price_with = db.Column(db.Integer())
    new_price_without = db.Column(db.Integer())
    offset = db.Column(db.Integer())
    panels = db.Column(db.Integer())
    loan_provider = db.Column(db.String(80))
    interest_rate = db.Column(db.String(10))
    re_roof = db.Column(db.Boolean())
    date_sold = db.Column(db.String(30))
    notes = db.Column(db.String(300))


    def __init__(self, sold_id, new_price_with, new_price_without, offset, panels, loan_provider, interest_rate, re_roof, date_sold, notes):
        self.sold_id = sold_id
        self.new_price_with = new_price_with
        self.new_price_without = new_price_without
        self.offset = offset
        self.panels = panels
        self.loan_provider = loan_provider
        self.interest_rate = interest_rate
        self.re_roof = re_roof
        self.date_sold = date_sold
        self.notes = notes

# def connect_to_db(app):
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://Jaxson:sqlpassword@localhost:5432/capstone-final'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     db.app = app
#     db.init_app(app)


# if __name__ == "__main__":
#     app = Flask(__name__)
#     connect_to_db(app)
#     db.create_all()
#     print("Connected to database")
