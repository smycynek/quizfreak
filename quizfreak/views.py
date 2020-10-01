"""
Quiz views
"""
import datetime
from rest_framework.response import Response
from rest_framework import status, mixins
from rest_framework.viewsets import GenericViewSet
from django.shortcuts import get_object_or_404
from .serializers import QuizSerializer, QuestionSerializer, ResultSerializer
from .models import Quiz, Question, Result

class QuizzesView(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    """
    Quizzes view
    """
    queryset = Quiz.objects.filter(locked__isnull=False, public=True)
    serializer_class = QuizSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = get_object_or_404(Quiz, pk=kwargs['pk'])
        if instance.locked is None:
            return Response("Quiz not yet locked", status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class QuestionsView(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
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
                      GenericViewSet):
    """
    Results view
    """
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

class QuizLockView(GenericViewSet):
    """
    Lock a quiz to make it read-only
    """
    def create(self, request, *args, **kwargs):
        """
        Set lock
        """
        quiz = Quiz.objects.all().get(id=kwargs['id'])
        if quiz.locked:
            return Response("Quiz already locked.", status=status.HTTP_403_FORBIDDEN)
        param_public = request.GET.get('public')
        if param_public and param_public.lower() == "false":
            quiz.public = False
        quiz.locked = datetime.datetime.now()
        quiz.save()
        return Response(status=status.HTTP_200_OK)
