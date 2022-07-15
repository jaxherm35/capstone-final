from re import template
from flask import Flask, redirect, render_template, url_for, Blueprint
from flask_debugtoolbar import DebugToolbarExtension
import jinja2
# from Project.model import connect_to_db
# from flask_wtf import AddForm
from Project import app
from Project.model import *

my_blueprint = Blueprint("solar_db", __name__, template_folder = "templates")


@my_blueprint.route('/sales', methods=['GET'])
def add_sales():

    # form = AddForm()
    # return redirect(url_for('sales_page'))
    return render_template('sales.html')


@my_blueprint.route('/sits', methods=['GET'])
def sits():
    # return redirect(url_for('sits_page'))
    return render_template('sits.html')


@my_blueprint.route('/add_sit', methods=['GET','POST'])
def add_sit():

    return render_template('add_sit.html')


@my_blueprint.route('/add_sale', methods=['GET', 'POST'])
def add_sale():

    return render_template('add_sale.html')
