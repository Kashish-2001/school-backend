from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView
from .models import Student, Classroom
from .serializers import StudentSerializer, ClassroomSerializer


class StudentCreateAPIView(CreateAPIView):
    serializer_class = StudentSerializer
    model = Student
    queryset = Student.objects.all()


class StudentListAPIView(ListAPIView):
    serializer_class = StudentSerializer
    model = Student
    queryset = Student.objects.all()


class StudentDetailAPIView(RetrieveAPIView):
    serializer_class = StudentSerializer
    model = Student
    queryset = Student.objects.all()


class StudentDeleteAPIView(DestroyAPIView):
    serializer_class = StudentSerializer
    model = Student
    queryset = Student.objects.all()