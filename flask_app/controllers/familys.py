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
    return render_template('user_hive.html', user = User.get_by_id(data), family = Family.get_all_by_users_id(data))

@app.route('/new_member')
def new_member():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('new_member.html')

@app.route('/new_member/new', methods=['POST'])
def new_member_new():
    if not Family.validate_new_member(request.form):
        return redirect('/new_member')
    data ={
        "generation": request.form['generation'],
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "place_of_birth": request.form['place_of_birth'],
        "date_of_birth": request.form['date_of_birth'],
        "age": request.form['age'],
        "users_id": session['user_id']
    }
    Family.save(data)
    return redirect('/hive')

@app.route('/show_member/<int:fm_id>')
def show_member(fm_id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id" : fm_id
    }    
    return render_template('show_member.html', family = Family.get_by_id(data))

@app.route('/edit_member/<int:fm_id>')
def edit_member(fm_id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id" : fm_id
    }    
    return render_template('edit_member.html', id = data, family = Family.get_by_id(data))

@app.route('/edit_member/<int:fm_id>/update', methods=['POST'])
def edit_member_update(fm_id):
    id = fm_id
    if not Family.validate_edit_member(request.form):
        return redirect(f'/edit_member/{id}')
    data = {
        "generation": request.form['generation'],
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "place_of_birth": request.form['place_of_birth'],
        "date_of_birth": request.form['date_of_birth'],
        "age": request.form['age'],
        "id": request.form['id']
        }
    Family.update(data)
    return redirect(f'/show_member/{id}')

@app.route('/delete_member/<int:fm_id>')
def delete_member(fm_id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id" : fm_id
    }
    Family.delete(data)
    return redirect('/hive')