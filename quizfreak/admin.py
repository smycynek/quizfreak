"""
Admin
"""
from django.contrib import admin
from .models import Quiz, Question, Result

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Result)
