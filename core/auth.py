from flask import *
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from flask_login import login_user, logout_user

auth = Blueprint('auth', __name__)

@auth.route('/signup/')
def signup():

    return render_template('signup.html')

@auth.route('/signup/', methods=['POST'])
def signup_auth():

    email = request.form.get('email')
    name = request.form.get('username')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    user = User.query.filter_by(email=email).first()

    if user:

        flash('A user with that email already exists.', category='error')

        return redirect(url_for('auth.signup'))

    elif len(email) < 7:

        flash('Your email must have more than 7 characters.', category='error')

        return redirect(url_for('auth.signup'))

    elif len(name) < 5:

        flash('Your name must have more than 5 characters.', category='error')

        return redirect(url_for('auth.signup'))

    elif len(password1) < 5 and len(password2) < 5:

        flash('Your password is too weak!', category='error')

        return redirect(url_for('auth.signup'))

    elif password1 != password2:

        flash("Your passwords don't match!", category='error')

        return redirect(url_for('auth.signup'))

    new_user = User(email=email, name=name, password=generate_password_hash(password1, method='sha256'))

    db.session.add(new_user)
    db.session.commit()

    flash('Your account has been created successfully.', category='success')

    return redirect(url_for('auth.login'))

@auth.route('/login/')
def login():

    return render_template('login.html')

@auth.route('/login/', methods=['POST'])
def login_auth():

    email = request.form.get('email')
    password = request.form.get('password')
    remember_me = True if request.form.get('remember') else None

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):

        flash('Wrong password or email. Please try again.', category='error')

        return redirect(url_for('auth.login'))

    login_user(user, remember=remember_me)

    flash('Logged in successfully!', category='success')

    return redirect(url_for('views.dashboard'))

@auth.route('/logout/')
def logout():

    logout_user()

    flash('Logged out successfully!', category='success')

    return redirect(url_for('auth.login'))