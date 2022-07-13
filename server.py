# from xmlrpc.client import _HostType
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db



app = Flask(__name__)
app.secret_key = "very_secret_key"

if __name__ == '__main__':
    app.env = 'development'
    connect_to_db(app)
    DebugToolbarExtension(app)
    app.run(port=5432, host='localhost', debug=True)    