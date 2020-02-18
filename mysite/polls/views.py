from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def foo(request):
    return HttpResponse("<div><h1>This renders as large text :0</h1></div>")

"""
    Guessing that whatever is returned can be html-views, or just strings is
    cool too.
"""
