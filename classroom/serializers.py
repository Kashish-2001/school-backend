from .models import Student, Classroom
from rest_framework.serializers import ModelSerializer


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'admission_number', 'is_qualified', 'average_score')


class ClassroomSerializer(ModelSerializer):
    students = StudentSerializer(many=True)

    class Meta:
        model = Classroom
        fields = ('name', 'student_capacity', 'students')
