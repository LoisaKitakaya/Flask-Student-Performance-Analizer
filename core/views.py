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

@views.route('/dashboard/<int:id>/')
def student_details(id):

    this_student = Student.query.filter_by(id=id).first()

    the_grades = Grades.query.filter_by(student_id=id).all()

    return render_template('dash_details.html', logged_user=current_user.name,student=this_student, grades=the_grades)

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

@views.route('/edit_student/<int:id>/', methods=['POST'])
def edit_student(id):

    this_student = Student.query.get_or_404(id)

    firstname = request.form.get('firstname')
    secondname = request.form.get('secondname')
    age = request.form.get('age')
    year = request.form.get('year')
    gender = request.form.get('gender')

    this_student.firstname = firstname
    this_student.secondname = secondname
    this_student.age = age
    this_student.year = year
    this_student.gender = gender

    db.session.add(this_student)
    db.session.commit()

    flash('Student record has been edited successfully.', category='success')

    return redirect(url_for('views.dashboard'))

@views.route('/delete_student/<int:id>/')
def delete_student(id):

    this_student = Student.query.get_or_404(id)

    db.session.delete(this_student)
    db.session.commit()

    flash('Student record has been deleted successfully.', category='success')

    return redirect(url_for('views.dashboard'))

@views.route('/add_grades/', methods=['POST'])
def add_grades():

    science = request.form.get('science')
    technology = request.form.get('technology')
    engineering = request.form.get('engineering')
    math = request.form.get('math')
    history = request.form.get('history')
    philosophy = request.form.get('philosophy')
    language = request.form.get('language')
    semester = request.form.get('semester')
    year = request.form.get('year')
    student_id = request.form.get('student_id')

    new_student_grades = Grades(science=science, technology=technology, engineering=engineering, math=math, history=history, philosophy=philosophy, language=language, semester=semester, year=year, student_id=student_id)

    db.session.add(new_student_grades)
    db.session.commit()

    flash('Grades have been added successfully.', category='success')

    return redirect(url_for('views.dashboard'))

@views.route('/edit_grades/<int:id>/', methods=['POST'])
def edit_grades(id):

    edited_grades = Grades.query.get_or_404(id)

    science = request.form.get('science')
    technology = request.form.get('technology')
    engineering = request.form.get('engineering')
    math = request.form.get('math')
    history = request.form.get('history')
    philosophy = request.form.get('philosophy')
    language = request.form.get('language')
    semester = request.form.get('semester')
    year = request.form.get('year')

    edited_grades.science = science
    edited_grades.technology = technology
    edited_grades.engineering = engineering
    edited_grades.math = math
    edited_grades.history = history
    edited_grades.philosophy = philosophy
    edited_grades.language = language
    edited_grades.semester = semester
    edited_grades.year = year

    db.session.add(edited_grades)
    db.session.commit()

    flash('Grades have been edited successfully.', category='success')

    return redirect(url_for('views.dashboard'))

@views.route('/delete_grades/<int:id>/')
def delete_grades(id):

    the_grades = Grades.query.get_or_404(id)

    db.session.delete(the_grades)
    db.session.commit()

    flash('Student grades have been deleted successfully.', category='success')

    return redirect(url_for('views.dashboard'))