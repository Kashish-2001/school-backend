import pytest
import random
from classroom.models import Student, Classroom


@pytest.fixture
def student_model(db):
    student = Student.objects.create(first_name="Emma", admission_number=123, is_qualified=True)
    return student


def test_student_can_be_created(student_model):
    student = Student.objects.last()
    assert student.first_name == student_model.first_name


def test_student_str_return(student_model):
    student = Student.objects.last()
    assert str(student) == student_model.first_name + str(student_model.admission_number)


def test_grade_fail(student_model):
    student_model.average_score = random.randint(0, 40)
    student_model.save()
    student = Student.objects.last()
    assert student.get_grade() == "Fail"


def test_grade_pass(student_model):
    student_model.average_score = random.randint(40, 75)
    student_model.save()
    student = Student.objects.last()
    assert student.get_grade() == "Pass"


def test_grade_excellent(student_model):
    student_model.average_score = random.randint(75, 101)
    student_model.save()
    student = Student.objects.last()
    assert student.get_grade() == "Excellent"


def test_grade_error(student_model):
    student_model.average_score = random.randint(101, 9999999)
    student_model.save()
    student = Student.objects.last()
    assert student.get_grade() == "Error"


def test_classroom_can_be_created(student_model):
    classroom = Classroom.objects.create(name="Physics", student_capacity=30)
    classroom.students.add(student_model)
    classroom.save()

    classroom_result = Classroom.objects.last()
    assert classroom.name == classroom_result.name

