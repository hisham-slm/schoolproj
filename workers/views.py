from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def workers_index(request):
    return HttpResponse("Hello workers")