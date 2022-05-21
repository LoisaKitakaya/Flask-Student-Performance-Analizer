from .models import Student, Grades
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

class AllGrades(Resource):

    def get(self):

        grades = Grades.query.all()

        grades_schema = GradeSchema(many=True)

        result = grades_schema.dump(grades)

        return jsonify({'data': result})

class GradesPerSem(Resource):

    def get(self):

        grades_sem1 = Grades.query.filter_by(semester=1).all()

        grades_sem2 = Grades.query.filter_by(semester=2).all()

        grades_sem3 = Grades.query.filter_by(semester=3).all()

        grades_schema = GradeSchema(many=True)

        result_sem1 = grades_schema.dump(grades_sem1)

        result_sem2 = grades_schema.dump(grades_sem2)

        result_sem3 = grades_schema.dump(grades_sem3)

        return jsonify({
            'data': {
                'sem1': result_sem1,
                'sem2': result_sem2,
                'sem3': result_sem3
            }
        })

        