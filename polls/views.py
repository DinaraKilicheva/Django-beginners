from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(request):
    return HttpResponse("<h1>Hello Django from <span style ='color:red'> p10</span></h1>")
