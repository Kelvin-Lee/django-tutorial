from django.urls import path

from . import views

"""

    The tutorial describes the urlpatterns as a "table of contents"
    to the website being served by Django

"""

urlpatterns = [
    path('', views.index, name='index'),
    path('foo', views.foo, name='Does this name matter?'),
]

"""

   Looks like this path() call is the same as in mysite/mysite/urls.py.
   The first param to path() is like a portion of a url. Second param
   seems to be functions that return HttpResponse()'s that are defined
   in mysite/polls/views.py i.e. the file that is imported here as 
   `views` on LOC 3.

"""
