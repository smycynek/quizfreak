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

        fields = ('id', 'name', 'description', 'index', 'quiz_id')

class QuizSerializer(serializers.ModelSerializer):
    """
    Quiz serializer
    """
    def get_results(self, instance):
        """ Serialize results by index order """
        results = instance.results.all().order_by('index')
        return ResultSerializer(results, many=True).data

    questions = QuestionSerializer(read_only=True, many=True)
    results = serializers.SerializerMethodField()
    locked = serializers.DateTimeField(read_only=True)
    public = serializers.BooleanField(required=False)
    class Meta:
        model = Quiz
        fields = ('id', 'name', 'questions', 'results', 'locked', 'public')
