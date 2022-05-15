from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():

    app = Flask(__name__)

    app.config['SECRET_KEY'] = '08sd09fnwrelsdf809s8wnrwlkesd8fwjlkr5jw'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    return app

def create_db(app):

    import os

    if not os.path.exists('core/' + DB_NAME):

        db.create_all(app=app)

        print(f"Database: '{DB_NAME}', has been create!")