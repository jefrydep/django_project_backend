from django.shortcuts import render

# importamos httt respnse
# luego vamos a urls.py

from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse('welocme to my server')


def about(request):
    return HttpResponse('about me')

