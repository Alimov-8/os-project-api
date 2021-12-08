from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('quiz.urls')),
    path('student/', include('accounts.urls')),
    path('', admin.site.urls),
]

admin.site.site_header = "Quiz System Admin"
admin.site.site_title = "Quiz System Admin Portal"
admin.site.index_title = "Welcome to Quiz Project Portal!"
