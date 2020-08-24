"""
Quiz serializers
"""

from rest_framework import serializers
from .models import Quiz, Question, Result

class QuestionSerializer(serializers.ModelSerializer):
    """
    Question serializer
    """
    quiz_id = serializers.PrimaryKeyRelatedField(source='quiz',
                                                     queryset=Quiz.objects.all(),
                                                     required=True,
                                                     allow_null=False)

    class Meta:
        model = Question
        fields = ('id', 'text', 'choices', 'quiz_id')


class ResultSerializer(serializers.ModelSerializer):
    """
    Results serializer
    """
    quiz_id = serializers.PrimaryKeyRelatedField(source='quiz',
                                                 queryset=Quiz.objects.all(),
                                                 required=True)
    class Meta:
        model = Result

        fields = ('id', 'name', 'description', 'quiz_id')

class QuizSerializer(serializers.ModelSerializer):
    """
    Quiz serializer
    """

    questions = QuestionSerializer(read_only=True, many=True)
    results = ResultSerializer(many=True, read_only=True)
    class Meta:
        model = Quiz
        fields = ('id', 'name', 'questions', 'results')
