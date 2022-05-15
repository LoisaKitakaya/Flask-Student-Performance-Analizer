from . import db

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def __repr__(self) -> str:
        
        return f'Username: {self.name}'

class Student(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
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
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))

    def __repr__(self) -> str:
        
        return f'Grades for user with id: {str(self.student_id)}'
