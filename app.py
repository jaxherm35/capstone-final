from flask import Flask, redirect, render_template, url_for

from Project import app

@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/home', methods=['GET'])
def home():
    test = ['test 1 ', 'test 2 ', 'test 3']
    return render_template('home.html', test=test)

if __name__ == '__main__':
    app.run(debug=True)


