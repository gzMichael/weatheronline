import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'qwonline_secret_key'

SQLALCHEMY_DATABASE_URI = 'sqlite:////history.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True