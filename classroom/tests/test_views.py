import pytest
from classroom.models import Student, Classroom
from rest_framework.test import APIClient
from rest_framework.reverse import reverse

@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def student_model(db):
    student1 = Student.objects.create(first_name="Emma", admission_number=123, is_qualified=True)
    # student2 = Student.objects.create(first_name="Mike", admission_number=121, is_qualified=True)
    return student1


def test_student_list_view(api_client, student_model):
    student1 = student_model
    student2 = Student.objects.create(first_name="Mike", admission_number=121, is_qualified=True)

    url = reverse("student_list_api")
    response = api_client.get(url)
    assert len(response.json()) == len(Student.objects.all())


@pytest.mark.django_db
def test_student_create_view(api_client):
    student_data = {
        "first_name": "Ross",
        "last_name": "Geller",
        "admission_number": 29,
        "is_qualified": False,
        "average_score": 2
    }
    url = reverse("student_create_api")
    response = api_client.post(url, student_data)
    assert response.json() != None
    assert response.status_code == 201
    assert Student.objects.count() == 1


def test_student_detail_view(api_client, student_model):
    url = reverse("student_detail_api", kwargs={"pk":student_model.pk})
    response = api_client.get(url)
    assert student_model.first_name == response.json()['first_name']


def test_student_delete_view(api_client, student_model):
    url = reverse("student_delete_api", kwargs={"pk":student_model.pk})
    response = api_client.delete(url)
    assert Student.objects.count() == 0
    assert response.status_code == 204