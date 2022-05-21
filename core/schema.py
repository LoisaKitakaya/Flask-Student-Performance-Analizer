from . import ma
from .models import Student, Grades

class StudentSchema(ma.SQLAlchemyAutoSchema):

    class Meta:

        model = Student

class GradeSchema(ma.SQLAlchemyAutoSchema):

    class Meta:

        model = Grades