"""
Quiz views
"""
from rest_framework.response import Response
from rest_framework import status, mixins
from rest_framework.viewsets import GenericViewSet
from .serializers import QuizSerializer, QuestionSerializer, ResultSerializer
from .models import Quiz, Question, Result

class QuizzesView(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    """
    Quizzes view
    """
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuestionsView(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    """
    Questions view
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def create(self, request, *args, **kwargs):
        serializer = QuestionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        return Response({"id": obj.id}, status=status.HTTP_201_CREATED)

class ResultsView(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    """
    Results view
    """
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
