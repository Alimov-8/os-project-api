from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.response import Response

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
        questions = Question.objects.filter(quiz=quiz_id)
        questions_list = list()
        choices_list = list()
        for q in questions:
            questions_list.append({
                'question': q.question,
                'choices': list(q.choice.values('choice_id', 'choice')),
                'correct_answer': q.choice.filter(is_correct_answer=True).values('choice_id').first()["choice_id"]
            })
            
        return Response({'questions': questions_list,})


# 127.0.0.1:8000/subjects/2/quizzes/3/questions

"""
{"questions" : 
    [
        { 
            "question": "Q1", 
            "choices" : [
                "choice_1": "A1",
                "choice_2": "A2",
                "choice_3": "A3",
                "choice_4": "A4",
            ]
            "correct_answer": 1,}
        },
        { 
            "question": "Q2", 
            "choices" : [
                "choice_1": "A1",
                "choice_2": "A2",
                "choice_3": "A3",
                "choice_4": "A4",
            ]
            "correct_answer": 3,}
        }
    ]
}
"""
