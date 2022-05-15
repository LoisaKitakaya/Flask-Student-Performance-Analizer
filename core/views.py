from flask import *

views = Blueprint('views', __name__)

@views.route('/', methods=['POST, GET'])
def dashboard():

    return render_template('index.html')