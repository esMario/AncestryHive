from flask import render_template, redirect, session, request
from flask_app import app
from flask_bcrypt import Bcrypt


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/hive')
def hive():
    return render_template('user_hive.html')