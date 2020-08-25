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

    def validate_quiz_id(self, value):
        """ validatation """
        if value.locked:
            raise serializers.ValidationError(f"quiz locked at {value.locked}")
        return value

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
    def validate_quiz_id(self, value):
        """ validatation """
        if value.locked:
            raise serializers.ValidationError(f"quiz locked at {value.locked}")
        return value

    class Meta:
        model = Result

        fields = ('id', 'name', 'description', 'quiz_id')

class QuizSerializer(serializers.ModelSerializer):
    """
    Quiz serializer
    """
    questions = QuestionSerializer(read_only=True, many=True)
    results = ResultSerializer(many=True, read_only=True)
    locked = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Quiz
        fields = ('id', 'name', 'questions', 'results', 'locked')
