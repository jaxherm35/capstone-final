# from xmlrpc.client import _HostType
import re
from flask import Flask, redirect, render_template, url_for
from flask_debugtoolbar import DebugToolbarExtension
import jinja2
# from flask_wtf import AddForm
import os 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://Jaxson:sqlpassword@localhost:5432/capstone-final'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)
app.secret_key = "very_secret_key"
app.config['SECRET_KEY'] = "very_secret_key"

app.jinja_env.undefined = jinja2.StrictUndefined

login_manager = LoginManager()
login_manager.init_app(app)

basedir = os.path.abspath(os.path.dirname(__file__))

from Project.Blueprints.view import my_blueprint
app.register_blueprint(my_blueprint, url_prefix="/solar_db")