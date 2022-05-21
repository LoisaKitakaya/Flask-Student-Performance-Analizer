from .models import Student, Grades, list_to_dict
from flask_restful import Resource, abort, fields, marshal_with
from flask import jsonify
from .schema import StudentSchema, GradeSchema

student_fields = {
    'id': fields.Integer,
    'first name': fields.String,
    'second name': fields.String,
    'age': fields.Integer,
    'year': fields.Integer,
    'gender': fields.String
}

grade_fields = {
    'id': fields.Integer,
    'science': fields.Integer,
    'technology': fields.Integer,
    'engineering': fields.Integer,
    'math': fields.Integer,
    'history': fields.Integer,
    'philosophy': fields.Integer,
    'language': fields.Integer,
    'semester': fields.Integer,
    'year of study': fields.Integer,
    'student id': fields.Integer
}

class GetAllStudents(Resource):

    def get(self):

        students = Student.query.all()

        student_schema = StudentSchema(many=True)

        result = student_schema.dump(students)

        return jsonify(result)

class GetStudent(Resource):

    @marshal_with(student_fields)
    def get(self, id):

        student = Student.query.filter_by(id=id).first()

        if not student:

            abort(404, message=f'Could not find user with id {id}.')

        return student

class GetStudentGrades(Resource):

    def get(self, id):

        grades = Grades.query.filter_by(student_id=id).all()

        grades_schema = GradeSchema(many=True)

        result = grades_schema.dump(grades)

        return jsonify(result)



        