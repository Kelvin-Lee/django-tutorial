"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

"""

    The tutorial describes the urlpatterns as a "table of contents"
    to the website being served by Django

"""

urlpatterns = [
    path('boop/', include('polls.urls')),
    path('admin/', admin.site.urls),
]

"""
   "
    The **include()** function allows referencing other URLconfs. Whenever
    Django encounters **include()**, it chops off whatever part of the URL
    matched up to that point and sends the remaining string to the included
    URLconf for further processing
                                                                            " 
                                                                - Tutorial

    This is why we can have another "table of contents" in mysite/polls/urls.py.
    Say we want to navigate to localhost:8000/boop/foo. This table of contents 
    (mysite/mysite/urls.py) will first match with "boop/", and then send "foo"
    to the next table of contents that is include()'d, which would be
    mysite/polls/urls.py
    localhost:8000/boop/
"""

"""
   It looks like the first param to path() matches the trailing part of
   the url e.g. in the url localhost:8000/polls, the trailing part is the
   "polls/"

   It's fine to change this param to something like "boop", but it'd mean
   that to be served whatever is in polls.urls, we'd have to navigate to
   localhost:8000/boop
"""
