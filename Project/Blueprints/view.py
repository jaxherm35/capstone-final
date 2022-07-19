from audioop import avg
from ctypes import addressof
from datetime import date
from doctest import register_optionflag
from hashlib import new
from re import L, S, sub, template
from unicodedata import name
from flask import Flask, redirect, render_template, url_for, Blueprint
from flask_debugtoolbar import DebugToolbarExtension
import jinja2
# from Project.model import connect_to_db
# from flask_wtf import AddForm
from Project import app
from Project.Blueprints.forms import AddUser, AddHomeowner, AddSit, AddSale
from Project.model import *

my_blueprint = Blueprint("solar_db", __name__, template_folder = "templates")


@my_blueprint.route('/sales', methods=['GET'])
def sales():

    return render_template('sales.html')


@my_blueprint.route('/sits', methods=['GET'])
def sits():
    
    return render_template('sits.html')

@my_blueprint.route('/add_homeowner', methods=['GET', 'POST'])
def add_homeowner():

    
    name = None
    address = None
    phone_number = None
    email = None
    avg_bill = None
    total_kwh = None

    form = AddHomeowner()
    
    if form.validate_on_submit():
        name = form.name.data
        address = form.homeowner_address.data
        phone_number = form.homeowner_phone_number.data
        email = form.homeowner_email.data
        avg_bill = form.homeowner_avg_bill.data
        total_kwh = form.homeowner_total_kwh.data
        # submit_homeowner = form.homeowner_submit_homeowner.data

        form.name.data = ''
        form.address.data = ''
        form.phone_number.data = ''
        form.email.data = ''
        form.avg_bill.data = ''
        form.total_kwh.data = ''
   
    return render_template('add_homeowner.html', form=form, name=name, address=address, phone_number=phone_number, email=email, avg_bill=avg_bill, total_kwh=total_kwh)

@my_blueprint.route('/add_sit', methods=['GET','POST'])
def add_sit():

    new_price_with = None
    new_price_without = None
    offset = None
    panels = None
    notes = None

    form = AddSit()

    if form.validate_on_submit():
        new_price_with = form.new_price_with.data
        new_price_without = form.new_price_without.data
        offset = form.offset.data
        panels = form.panels.data
        notes= form.notes.data

        form.new_price_with = ''
        form.new_price_without = ''
        form.offset = ''
        form.panels = ''
        form.notes = ''

    return render_template('add_sit.html', form=form, new_price_with=new_price_with, new_price_without=new_price_without, offset=offset, panels=panels, notes=notes)


@my_blueprint.route('/add_sale', methods=['GET', 'POST'])
def add_sale():

    new_price_with = None
    new_price_without = None
    offset = None
    panels = None
    loan_provider = None
    interest_rate = None
    re_roof = None
    date_sold = None

    form = AddSale()

    if form.validate_on_submit():
        new_price_with = form.new_price_with.data
        new_price_without = form.new_price_without.data
        offset = form.offset.data
        panels = form.panels.data
        loan_provider = form.loan_provider.data
        interest_rate = form.interest_rate.data
        re_roof = form.re_roof.data
        date_sold = form.date_sold.data

        form.new_price_with = ''
        form.new_price_without = ''
        form.offset = ''
        form.panels = ''
        form.loan_provider = ''
        form.interest_rate = ''
        form.re_roof = ''
        form.date_sold = ''

    return render_template('add_sale.html', form=form, new_price_with=new_price_with, new_price_without=new_price_without, offset=offset, panels=panels, loan_provider=loan_provider, interest_rate=interest_rate, re_roof=re_roof, date_sold=date_sold)
