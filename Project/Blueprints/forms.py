# from ast import In
# from datetime import date
# from tokenize import String
# from unicodedata import name
# from xmlrpc.client import Boolean
from flask import Flask
from flask_wtf import FlaskForm
from sqlalchemy import Integer
from wtforms import StringField, SubmitField, IntegerField, BooleanField


class AddUser(FlaskForm):

    name = StringField()



class AddHomeowner(FlaskForm):
    
    name = StringField()
    address = StringField()
    phone_number = StringField()
    email = StringField()
    avg_bill = StringField()
    total_kwh = StringField()


class AddSit(FlaskForm):

    new_price_with = IntegerField()
    new_price_without = IntegerField()
    offset = IntegerField()
    panels = IntegerField()
    notes = StringField()


class AddSales(FlaskForm):

    new_price_with = IntegerField()
    new_price_without = IntegerField()
    offset = IntegerField()
    panels = IntegerField()
    loan_provider = StringField()
    interest_rate = StringField()
    re_roof = BooleanField()
    date_sold = StringField()
    notes = StringField()
