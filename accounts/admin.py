from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from .models import Student


@admin.register(Student)
class StudentAdmin(ModelAdmin):
    list_display = [
        'username',
        'password',
    ]
    