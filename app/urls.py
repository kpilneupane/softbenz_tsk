from django.urls import path
from . import views

urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    path('students', views.StudentView.as_view(), name='student_list'),
    path('courses', views.CourseView.as_view(), name='course_list')
]
