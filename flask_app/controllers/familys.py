from flask import render_template, redirect, session, request
from flask_app.models.family import Family
from flask_app.models.user import User
from flask_app import app



@app.route('/hive')
def hive():
    if 'user_id' not in session:
        return redirect('/logout')    
    data ={
        'id': session['user_id']
    }     
    return render_template('user_hive.html', user = User.get_by_id(data))

@app.route('/new_member')
def new_member():
    if 'user_id' not in session:
        return redirect('/logout')   
    return render_template('new_member.html')