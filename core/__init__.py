from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_restful import Api
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

DB_NAME = 'database.db'

def create_app():

    app = Flask(__name__)

    app.config['SECRET_KEY'] = '08sd09fnwrelsdf809s8wnrwlkesd8fwjlkr5jw'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    ma.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    api = Api(app)

    from .endpoints import GetStudent, GetStudentGrades, GetAllStudents

    api.add_resource(GetStudent, '/student/<int:id>/')
    api.add_resource(GetStudentGrades, '/student/grades/<int:id>/')
    api.add_resource(GetAllStudents, '/all_students/')

    from .models import User

    create_db(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):

        return User.query.get(int(user_id))

    return app

def create_db(app):

    import os

    if not os.path.exists('core/' + DB_NAME):

        db.create_all(app=app)

        print(f"Database: '{DB_NAME}', has been create!")