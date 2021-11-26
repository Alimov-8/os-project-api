from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from quiz.models import *


@admin.register(Subject)
class SubjectAdmin(ModelAdmin):
    pass


@admin.register(Quiz)
class QuizAdmin(ModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(ModelAdmin):
    pass


class MyAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy('OS Project - Quiz Game Admin')

    # Text to put in each page's <h1> (and above login form).
    site_header = ugettext_lazy('OS Project - Quiz Game administration')

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('OS Project - Quiz Game administration')


admin_site = MyAdminSite()
