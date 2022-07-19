# from ast import In
# from datetime import date
# from tokenize import String
# from unicodedata import name
# from xmlrpc.client import Boolean
from flask import Flask
from flask_wtf import FlaskForm
from psycopg2 import DatabaseError
from sqlalchemy import Integer
from wtforms import StringField, SubmitField, IntegerField, BooleanField
from wtforms.validators import DataRequired


class AddUser(FlaskForm):

    name = StringField()



class AddHomeowner(FlaskForm):
    
    name = StringField('Homeowner name', validators=[DataRequired()])
    address = StringField('Homeowner address')
    phone_number = StringField('Homeowner phone number')
    email = StringField('Homeowner email')
    avg_bill = StringField('Homeowner avgerage bill')
    total_kwh = StringField('Homeowner total kwh')
    submit_homeowner = SubmitField('Add Homeowner')


class AddSit(FlaskForm):

    new_price_with = IntegerField()
    new_price_without = IntegerField()
    offset = IntegerField()
    panels = IntegerField()
    notes = StringField()


class AddSale(FlaskForm):

    new_price_with = IntegerField()
    new_price_without = IntegerField()
    offset = IntegerField()
    panels = IntegerField()
    loan_provider = StringField()
    interest_rate = StringField()
    re_roof = BooleanField()
    date_sold = StringField()
    notes = StringField()
