from click import confirm
from flask import Flask, redirect, render_template, url_for, flash
from requests import request
from Project.Blueprints.forms import AddUser, LoginForm
from Project import app
from Project.model import *
from Project import Blueprints
# from Project.__init__ import login_manager
from flask_login import current_user, login_user, login_required, logout_user, LoginManager
from Project.Blueprints.view import my_blueprint
from flask_bcrypt import Bcrypt, generate_password_hash, check_password_hash


bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

@app.route('/', methods=['GET', 'POST'])
def add_user():

    username = None
    password = None
    

    form = AddUser()

    if form.validate_on_submit():

        print('Successfully added user')
        username = form.username.data
        password = form.password.data
        
        
        new_user = Users(username=username, password=password)


        db.session.add(new_user)
        db.session.commit()
        flash('New User Added Successfully!')

        return redirect(url_for('home'))

    return render_template('add_user.html', form=form, username=form.username.data, password=password)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user:
            if user.password == form.password.data:
                login_user(user)
                return redirect(url_for('home'))

            else:
                flash('Invalid Password')
                print('Error logging in')
        
        else:
            flash('User does not exist')

    return render_template('login.html', form=form)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('User logged out successfully')
    return redirect(url_for('login'))

@app.route('/home', methods=['GET'])
@login_required
def home():
    return render_template('home.html')

@app.route('/test', methods=['GET'])
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)


