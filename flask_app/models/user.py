from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        return connectToMySQL('ancestryhive').query_db(query,data)

    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, password = %(password)s WHERE id = %(id)s"
        print(query)
        return connectToMySQL('ancestryhive').query_db(query,data)

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('ancestryhive').query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])    

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('ancestryhive').query_db(query,data)
        return cls(results[0])

    @staticmethod
    def validate_register(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('ancestryhive').query_db(query,user)
        
        if len(user['first_name']) < 2:
            flash("First name needs 2 characters or more", "user_register")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last name needs 2 characters or more", "user_register")
            is_valid = False
        if len(results) >= 1:
            flash("Email already in use", "user_register")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email", "user_register")
            is_valid=False
        if len(user['password']) < 8:
            flash("Password needs 8 characters or more", "user_register")
            is_valid = False
        if not any(char.isdigit() for char in user['password']):
            flash('Password should have at least one number', "user_register")
            is_valid = False
        if not any(char.isupper() for char in user['password']):
            flash('Password should have at least one uppercase letter', "user_register")
            is_valid = False
        if user['password'] != user['confirm']:
            flash("Comfirm password does not match", "user_register")
            is_valid = False
        return is_valid
    
    @staticmethod
    def validate_update(data):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('ancestryhive').query_db(query,data)
        
        if len(data['first_name']) < 2:
            flash("First name needs 2 characters or more", "user_edit")
            is_valid = False
        if len(data['last_name']) < 2:
            flash("Last name needs 2 characters or more", "user_edit")
            is_valid = False
        if len(results) >= 1:
            flash("Email already in use", "user_edit")
            is_valid=False
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email", "user_edit")
            is_valid=False
        if len(data['password']) < 8:
            flash("Password needs 8 characters or more", "user_edit")
            is_valid = False
        if not any(char.isdigit() for char in data['password']):
            flash('Password should have at least one number', "user_edit")
            is_valid = False
        if not any(char.isupper() for char in data['password']):
            flash('Password should have at least one uppercase letter', "user_edit")
            is_valid = False
        if data['password'] != data['confirm']:
            flash("Comfirm password does not match", "user_edit")
            is_valid = False
        return is_valid
        
    