"""
Quiz models
"""

import uuid
from django.db import models
from django.contrib.postgres import fields as django_fields


class Result(models.Model):
    """
    A quiz result object, e.g. 'type c personality', 'the strong silent type'
    """
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    name = models.CharField('name', max_length=200, null=False, blank=False)
    description  = models.CharField('description', max_length=200, null=False, blank=False)
    quiz = models.ForeignKey("quizfreak.Quiz", related_name='results',
        null=False, on_delete=models.deletion.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.description}, {self.id}"

class Question(models.Model):
    """
    A quiz question
    """
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    text = models.CharField('text', max_length=200, null=False, blank=False)
    choices = django_fields.ArrayField(models.CharField(max_length=200),
        null=False, blank=False)
    quiz = models.ForeignKey("quizfreak.Quiz", related_name='questions',
        null=False, on_delete=models.deletion.CASCADE)

    def __str__(self):
        return f"{self.text}, {self.choices}, {self.id}"

class Quiz(models.Model):
    """
    Basic quiz model
    """
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    name = models.CharField('name', max_length=200, null=False, blank=False)
    locked = models.DateTimeField('locked', null=True)

    def __str__(self):
        return f"{self.name}, {self.locked}, {self.id}"
