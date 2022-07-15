from datetime import date
from tokenize import String
from unicodedata import name
from flask import Flask
from flask_wtf import FlaskForm
from sqlalchemy import Integer
from wtforms import StringField, SubmitField, IntegerField


class AddUser(FlaskForm):

    name = StringField()


class AddSit(FlaskForm):

    name = StringField()
    address = StringField()
    phone_number = StringField()
    email = StringField()
    avg_bill_price = StringField()
    total_kwh = IntegerField()
    new_price_with_paydown = IntegerField()
    new_price_without_paydown = IntegerField()
    offset = IntegerField()
    panels = IntegerField()
    notes = StringField()


class AddSale(FlaskForm):

    name = StringField()
    address = StringField()
    phone_number = StringField()
    email = StringField()
    avg_bill_price = StringField()
    total_kwh = IntegerField()
    new_price_with_paydown = IntegerField()
    new_price_without_paydown = IntegerField()
    offset = IntegerField()
    panels = IntegerField()
    loan_provider= StringField()
    interest_rate = StringField()
    date_sold = StringField()
    notes = StringField()