#============================================================
#config.py
#============================================================

import os
basedir = os.path.abspath(os.path.dirname(__file__))

#tells the app where to find the database and how to login 
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/swamprdb'

#Monitor the amount of time a user has spent on the form
CSRF_ENABLED = True
SECRET_KEY = 'big-ol-secret'