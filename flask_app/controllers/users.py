from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.user import User

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/user_register', methods=['POST'])
def user_register():
    if not User.validate_register(request.form):
        return redirect('/login')
    data ={
        "full_name": request.form['full_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    session['user_id'] = id
    return redirect('/hive')

@app.route('/user_login', methods=['POST'])
def user_login():
    user = User.get_by_email(request.form)
    if not user:
        flash("Invalid Email/Password", "user_login")
        return redirect('/login')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Email/Password", "user_login")
        return redirect('/login')
    session['user_id'] = user.id
    return redirect('/hive')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')