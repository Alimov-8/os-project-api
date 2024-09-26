from django.urls import path

from .views import SubjectViewSet, QuizViewSet, QuestionViewSet
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register(r'subjects', SubjectViewSet)
router.register(r'quizzes', QuizViewSet)
router.register(r'questions', QuestionViewSet)

urlpatterns = [
    path('subjects/<int:subject_id>/quizzes/', views.get_subject_quizzes, name='subject-quizzes'),
    path('subjects/<int:subject_id>/quizzes/<int:quiz_id>/questions/', views.get_quiz_questions, name='quiz-questions'),
    path('quiz/<subject>/<quiz>/<username>/<score>/add/', views.add_user_score, name='add-score'),
    path('quiz/<subject>/<quiz>/all/results/', views.all_results, name='all-results'),
]

urlpatterns += router.urls
