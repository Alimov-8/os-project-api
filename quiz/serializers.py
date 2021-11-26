from rest_framework.serializers import ModelSerializer
from quiz.models import Subject, Quiz, Question


class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class QuizSerializer(ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
