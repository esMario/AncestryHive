from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

class Family:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.generation = data['generation']
        self.place_of_birth = data['place_of_birth']
        self.date_of_birth = data['date_of_birth']
        self.age = data['age']
        self.users_id = data['users_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save(cls,data):
        query = "INSERT INTO family_members (generation, first_name, last_name, place_of_birth, date_of_birth, age, users_id) VALUES(%(generation)s, %(first_name)s, %(last_name)s, %(place_of_birth)s, %(date_of_birth)s, %(age)s, %(users_id)s)"
        return connectToMySQL('ancestryhive').query_db(query,data)

    @classmethod
    def get_all_members(cls):
        query = "SELECT * FROM family_members"
        results = connectToMySQL('ancestryhive').query_db(query)
        members = []
        for family_members in results:
            members.append(cls(family_members))
        return members

    @classmethod
    def get_all_by_users_id(cls,data):
        query = "SELECT * FROM family_members WHERE users_id = %(id)s;"
        results = connectToMySQL('ancestryhive').query_db(query,data)
        members = []
        for family_members in results:
            members.append(cls(family_members))
        return members

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM family_members WHERE id = %(id)s;"
        results = connectToMySQL('ancestryhive').query_db(query,data)
        return results
    
    @classmethod
    def update(cls,data):
        query = "UPDATE family_members SET first_name = %(first_name)s, last_name = %(last_name)s, generation = %(generation)s, place_of_birth = %(place_of_birth)s, date_of_birth = %(date_of_birth)s, age = %(age)s WHERE id = %(id)s"
        print(query)
        return connectToMySQL('ancestryhive').query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM family_members WHERE id = %(id)s"
        return connectToMySQL('ancestryhive').query_db(query,data)


    @staticmethod
    def validate_new_member(data):
        is_valid = True
        results = connectToMySQL('ancestryhive').query_db(data)

        if len(data['generation']) < 2:
            flash("Genration is needed to build the hive.", "new_member")
            is_valid = False
        if len(data['first_name']) < 2:
            flash("First Name needs 2 characters or more", "new_member")
            is_valid = False
        if len(data['last_name']) < 2:
            flash("Last Name needs 2 characters or more", "new_member")
            is_valid = False            
        return is_valid
    
    @staticmethod
    def validate_edit_member(data):
        is_valid = True
        results = connectToMySQL('ancestryhive').query_db(data)

        if len(data['generation']) < 2:
            flash("Genration is needed to build the hive.", "edit_member")
            is_valid = False
        if len(data['first_name']) < 2:
            flash("First Name needs 2 characters or more", "edit_member")
            is_valid = False
        if len(data['last_name']) < 2:
            flash("Last Name needs 2 characters or more", "edit_member")
            is_valid = False            
        return is_valid
    