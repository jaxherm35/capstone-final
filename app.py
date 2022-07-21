from click import confirm
from flask import Flask, redirect, render_template, url_for
from Project.Blueprints.forms import AddUser
from Project import app
from Project.model import *

@app.route('/', methods=['GET', 'POST'])
def add_user():

    username = None
    password = None
    confirm = None

    form = AddUser()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        confirm = form.confirm.data


    return render_template('add_user.html', form=form, username=username, password=password, confirm=confirm)


@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)


