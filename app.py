# from xmlrpc.client import _HostType
import re
from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
import jinja2
from model import connect_to_db



app = Flask(__name__)
app.secret_key = "very_secret_key"

app.jinja_env.undefined = jinja2.StrictUndefined

if __name__ == '__main__':
    app.env = 'development'
    connect_to_db(app)
    DebugToolbarExtension(app)
    app.run(port=5432, host='localhost', debug=True)    


@app.route('/')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
        return render_template('home.html')

@app.route('/sales', methods=['GET', 'POST'])
def sales_page():
        return render_template('sales.html')
