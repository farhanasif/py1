from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homerun(request):
    return HttpResponse('<h1>Welcome Home.</h1>')


def about(request):
    return HttpResponse('<h1>About</h1>')
