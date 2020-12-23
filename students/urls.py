from django.urls import path
from . import views


urlpatterns = [
    path('students/', views.students, name='students'),
    path('student/add/', views.add_student, name="add-students"),
    path('schools/', views.schools, name="schools"),
    path('school/add/', views.add_school, name="add-schools"),
]
