from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from quiz.models import Quiz, Question, Subject, Choice, Results


class QuizInline(admin.TabularInline):
    model = Quiz
    extra = 1


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    
    
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


@admin.register(Subject)
class SubjectAdmin(ModelAdmin):
    list_display = [
        'name',
        'id',
    ]

    inlines = [
        QuizInline,
    ]


# @admin.register(Quiz)
# class QuizAdmin(ModelAdmin):
#     list_display = [
#         'name',
#         'subject',
#         'id',
#     ]


@admin.register(Question)
class QuestionAdmin(ModelAdmin):
    list_display = [
        'question',
        'quiz',
        'id',
    ]

    inlines = [
        ChoiceInline,
    ]


@admin.register(Results)
class ResultsAdmin(ModelAdmin):
    list_display = [
        'subject',
        'quiz',
        'username',
        'score',
    ]
