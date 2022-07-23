# from audioop import avg
# from ctypes import addressof
# from datetime import date
# from doctest import register_optionflag
# from hashlib import new
# from re import L, S, sub, template
# from unicodedata import name
# from crypt import methods
from flask import Flask, redirect, render_template, request, url_for, Blueprint
from flask_debugtoolbar import DebugToolbarExtension
import jinja2
# from Project.model import connect_to_db
# from flask_wtf import AddForm
from Project import app
from Project.Blueprints.forms import AddHomeowner, AddSit, AddSale
from Project.model import *
# from app import my_blueprint

my_blueprint = Blueprint("solar_db", __name__, template_folder = "templates")
# app.register_blueprint(my_blueprint, url_prefix="/solar_db")


@my_blueprint.route('/sales', methods=['GET'])
def sales():

    # sales = sales.query.all()
    
    return render_template('sales.html')


@my_blueprint.route('/sits', methods=['GET'])
def sits():
    
    # print(sits.query.all())

    return render_template('sits.html')

@my_blueprint.route('/homeowners', methods=['GET'])
def homeowners():

    return render_template('homeowners.html')

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
        print('Success')
        name = form.name.data
        address = form.address.data
        phone_number = form.phone_number.data
        email = form.email.data
        avg_bill = form.avg_bill.data
        total_kwh = form.total_kwh.data
            

        new_homeowner = Homeowner(name, address, phone_number, email, avg_bill, total_kwh)
        db.session.add(new_homeowner)
        db.session.commit()

        return redirect(url_for('solar_db.homeowners'))
    
    else: 
        print('curse words') 
   
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
