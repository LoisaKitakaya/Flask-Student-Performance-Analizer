from crypt import methods
from flask import *

views = Blueprint('views', __name__)

@views.route('/')
def home():

    return render_template('index.html')

@views.route('/dashboard/')
def dashboard():

    return render_template('dashboard.html')

@views.route('/admin/')
def admin():

    return render_template('admin.html')