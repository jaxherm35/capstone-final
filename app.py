# from xmlrpc.client import _HostType
import re
from flask import Flask, redirect, render_template, url_for
from flask_debugtoolbar import DebugToolbarExtension
import jinja2
from model import connect_to_db
from flask_wtf import AddForm 



app = Flask(__name__)
app.secret_key = "very_secret_key"

app.jinja_env.undefined = jinja2.StrictUndefined

if __name__ == '__main__':
    app.env = 'development'
    connect_to_db(app)
    DebugToolbarExtension(app)
    app.run(port=5432, host='localhost', debug=True)    


@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/home', methods=['GET'])
def home():
    test = ['test 1 ', 'test 2 ', 'test 3']
    return render_template('home.html', test=test)


@app.route('/sales', methods=['GET', 'POST'])
def add_sales():

    # form = AddForm()
    # return redirect(url_for('sales_page'))
    return render_template('sales.html')


@app.route('/sits', methods=['GET', 'POST'])
def sits():
    # return redirect(url_for('sits_page'))
    return render_template('sits.html')