from click import confirm
from flask import Flask, redirect, render_template, url_for, flash
from Project.Blueprints.forms import AddUser, LoginForm
from Project import app
from Project.model import *
from Project import Blueprints
# from Project.__init__ import login_manager
from flask_login import login_user, login_required, logout_user, current_user, LoginManager
from Project.Blueprints.view import my_blueprint
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return Users.get(int(user_id))

@app.route('/', methods=['GET', 'POST'])
def add_user():

    username = None
    password = None
    

    form = AddUser()

    if form.validate_on_submit():
        print('Successfully added user')
        username = form.username.data
        password = form.password.data
        

        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = Users(username=username, password=hashed_password)


        db.session.add(new_user)
        db.session.commit()
        flash('New User Added Successfully!')

        return redirect(url_for('home'))

    return render_template('add_user.html', form=form, username=form.username.data, password=password)



@app.route('/', methods=['GET', 'POST'])
def login():
    
    form = LoginForm()
    if form.validate_on_submit():   
        user = Users.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)

                return redirect(url_for('home'))

    return render_template('add_user.html', form=form, username=form.username.data, password=form.password.data)


@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/test', methods=['GET'])
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)


