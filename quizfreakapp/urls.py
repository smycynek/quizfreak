"""
Quiz urls
"""
from django.urls import include, path

urlpatterns = [
    path('', include('quizfreak.urls')),
]
