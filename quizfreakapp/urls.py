"""
Quiz urls
"""
from django.urls import include
from django.conf.urls import url
# from . import admin

urlpatterns = [
    url(r'^', include('quizfreak.urls')),

]
