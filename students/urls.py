from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('students/',views.students_index, name="stud_home"),
    path('students2/', views.students2_index, name='stud2_home')
]