from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def __repr__(self) -> str:
        
        return f'Username: {self.name}'

class Student(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100))
    secondname = db.Column(db.String(100))
    age = db.Column(db.Integer)
    year = db.Column(db.Integer)
    gender = db.Column(db.String(50))
    grades = db.relationship('Grades')

    def __repr__(self) -> str:
        
        return f'Student name: {self.name}'

class Grades(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    science = db.Column(db.Integer)
    technology = db.Column(db.Integer)
    engineering = db.Column(db.Integer)
    math = db.Column(db.Integer)
    history = db.Column(db.Integer)
    philosophy = db.Column(db.Integer)
    language = db.Column(db.Integer)
    semester = db.Column(db.Integer)
    year = db.Column(db.Integer)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))

    def __repr__(self) -> str:
        
        return f'Grades for user with id: {str(self.student_id)}'
