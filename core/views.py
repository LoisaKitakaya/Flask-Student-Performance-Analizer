from flask import *
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
def home():

    return render_template('index.html', logged_user=current_user)

@views.route('/dashboard/')
@login_required
def dashboard():

    return render_template('dashboard.html', logged_user=current_user.name)

@views.route('/admin/')
@login_required
def admin():

    return render_template('admin.html', logged_user=current_user.name)