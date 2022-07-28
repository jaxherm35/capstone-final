# from ast import In
# from datetime import date
# from tokenize import String
# from unicodedata import name
# from xmlrpc.client import Boolean
from ast import In
from click import password_option
from flask import Flask
from flask_wtf import FlaskForm
from psycopg2 import DatabaseError
from sqlalchemy import Integer
from wtforms import StringField, SubmitField, IntegerField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo 

class AddUser(FlaskForm):

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=7, max=25)])
    confirm = PasswordField('Confirm Password', validators=[DataRequired('Required'), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=7, max=25)])
    submit = SubmitField('Submit')


class AddHomeowner(FlaskForm):
    
    name = StringField('Homeowner name', validators=[DataRequired()])
    address = StringField('Homeowner address')
    phone_number = StringField('Homeowner phone number')
    email = StringField('Homeowner email')
    avg_bill = StringField('Homeowner avgerage bill')
    total_kwh = StringField('Homeowner total kwh')
    submit_homeowner = SubmitField('Add Homeowner')


class AddSit(FlaskForm):

    homeowner_id = IntegerField('Homeowner id', validators=[DataRequired()])
    new_price_with = IntegerField('New price with tax return paydown')
    new_price_without = IntegerField('New price without tax return paydown')
    offset = IntegerField('Offset percentage')
    panels = IntegerField('Total number of panels')
    notes = StringField('Homeowner notes')
    submit_sit = SubmitField('Add Sit')


class AddSale(FlaskForm):

    new_price_with = IntegerField('New price with tax return paydown')
    new_price_without = IntegerField('New price without tax return paydown')
    offset = IntegerField('Offset percentage')
    panels = IntegerField('Total number of panels')
    loan_provider = StringField('Loan provider')
    interest_rate = StringField('Interest rate')
    re_roof = BooleanField('Requires re-roof')
    date_sold = StringField('Date sold')
    notes = StringField('Homeowner notes')
    submit_sale = SubmitField('Add Sale')
