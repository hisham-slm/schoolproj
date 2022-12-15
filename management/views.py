from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def managemet_index(request):
    return HttpResponse("Welcome Management Team")