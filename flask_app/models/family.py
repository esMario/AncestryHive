from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

class Family:
    def __init__( self , data ):
        self.id = data['id']
        self.full_name = data['full_name']
        self.place_of_birth = data['place_of_birth']
        self.date_of_birth = data['date_of_birth']
        self.age = data['age']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']

