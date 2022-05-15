from flask import *
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User

auth = Blueprint('auth', __name__)

@auth.route('/signup/')
def signup():

    return render_template('signup.html')

@auth.route('/signup/', methods=['POST'])
def signup_auth():

    return redirect(url_for('auth.login'))

@auth.route('/login/')
def login():

    return render_template('login.html')

@auth.route('/login/', methods=['POST'])
def login_auth():

    return redirect(url_for('views.dashboard'))

@auth.route('/logout/')
def logout():

    return 'logout page.'