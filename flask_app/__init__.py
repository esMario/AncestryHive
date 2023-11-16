from flask import Flask

UPLOAD_FOLDER = '/static/images/member_imgs'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


app.secret_key = "@X5pB$eYw9nVdQmHr2kT6#vFtMqSxZzL"
from flask_app import app



