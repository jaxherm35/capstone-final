from audioop import avg
from ctypes import addressof
from hashlib import new
from re import S, sub, template
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

    return render_template('add_sit.html')


@my_blueprint.route('/add_sale', methods=['GET', 'POST'])
def add_sale():

    return render_template('add_sale.html')
