from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from quiz.models import Quiz, Question, Subject


class QuizInline(admin.TabularInline):
    model = Quiz
    extra = 1


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    fields = ('question', 'choice_1', 'choice_2', 'choice_3', 'correct_answer')


@admin.register(Subject)
class SubjectAdmin(ModelAdmin):
    list_display = [
        'id',
        'name',
    ]

    inlines = [
        QuizInline,
    ]


@admin.register(Quiz)
class QuizAdmin(ModelAdmin):
    list_display = [
        'id',
        'name',
        'subject',
    ]

    inlines = [
        QuestionInline,
    ]


# @admin.register(Question)
# class QuestionAdmin(ModelAdmin):
#     pass

