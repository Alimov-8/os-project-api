from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from quiz.models import Quiz, Question, Subject


class QuizInline(admin.TabularInline):
    model = Quiz


class QuestionInline(admin.TabularInline):
    model = Question


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

