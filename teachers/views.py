from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def teachers_index(request):
    return HttpResponse("Welcome Teachers")