from flask import *
from flask_login import login_required, current_user
from .models import Student, Grades
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def home():

    return render_template('index.html', logged_user=current_user)

@views.route('/dashboard/')
@login_required
def dashboard():

    students = Student.query.all()

    total_students = len(students)

    return render_template('dashboard.html', logged_user=current_user.name, all_students=students, total=total_students)

@views.route('/add_student/', methods=['POST'])
def add_student():

    firstname = request.form.get('firstname')
    secondname = request.form.get('secondname')
    age = request.form.get('age')
    year = request.form.get('year')
    gender = request.form.get('gender')

    new_student = Student(firstname=firstname, secondname=secondname, age=age, year=year, gender=gender)

    db.session.add(new_student)
    db.session.commit()

    flash('Student record has been added successfully.', category='success')

    return redirect(url_for('views.dashboard'))

@views.route('/admin/')
@login_required
def admin():

    return render_template('admin.html', logged_user=current_user.name)