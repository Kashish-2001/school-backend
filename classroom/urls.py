from django.urls import path
from .views import StudentCreateAPIView, StudentListAPIView, StudentDetailAPIView, StudentDeleteAPIView

urlpatterns = [
    path('student/list/', StudentListAPIView.as_view(), name="student_list_api"),
    path('student/create/', StudentCreateAPIView.as_view(), name="student_create_api"),
    path('student/<int:pk>/', StudentDetailAPIView.as_view(), name="student_detail_api"),
    path('student/<int:pk>/delete/', StudentDeleteAPIView.as_view(), name="student_delete_api"),
]
