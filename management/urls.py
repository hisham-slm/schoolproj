from django.urls import path
from . import views

urlpatterns=[
    path('', views.managemet_index)
]