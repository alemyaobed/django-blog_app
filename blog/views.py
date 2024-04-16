from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # Return this following response when the called.
    return HttpResponse('<h1>Blog Home!</h1>')
