from flask import *

auth = Blueprint('auth', __name__)

@auth.route('/signup/', methods=['POST, GET'])
def signup():

    return 'signup page.'

@auth.route('/login/', methods=['POST, GET'])
def login():

    return 'login page.'

@auth.route('/logout/', methods=['POST, GET'])
def logout():

    return 'logout page.'