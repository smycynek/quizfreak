"""
Quiz urls
"""
from rest_framework.routers import DefaultRouter
from django.urls import include, path
from django.contrib import admin
from . import views

# Create a router and register our viewsets with it.
ROUTER = DefaultRouter(trailing_slash=False)
ROUTER.register(r'quizzes', views.QuizzesView)
ROUTER.register(r'results', views.ResultsView)
ROUTER.register(r'questions', views.QuestionsView)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(ROUTER.urls)),
     path('admin/', admin.site.urls),
     path('quizzes/<uuid:id>/lock',
         views.QuizLockView.as_view({'post': 'create'}),
         name='quiz-lock'),
]
