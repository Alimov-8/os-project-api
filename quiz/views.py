from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view

from quiz.models import Subject, Quiz, Question
from .serializers import (
    SubjectSerializer,
    QuizSerializer,
    QuestionSerializer,
)


class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class QuizViewSet(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['subject']


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['question']


@api_view(['GET'])
def get_subject_quizzes(request, subject_id):
    """
    Returns all quizzes for the particular subject, with its subject ID
    """
    if request.method == 'GET':
        quizzes = Quiz.objects.all().filter(subject=subject_id).values()
        return JsonResponse({'quizzes': list(quizzes)})


@api_view(['GET'])
def get_quiz_questions(request, subject_id, quiz_id):
    """
    Returns the questions for the particular quiz, with its ID
    """
    if request.method == 'GET':
        questions = Question.objects.all().filter(quiz=quiz_id).values()
        return JsonResponse({'questions': list(questions)})

# 127.0.0.1:8000/subjects/2/quizzes/3/questions
