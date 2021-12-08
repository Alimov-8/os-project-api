from django.urls import path
from . import views


urlpatterns = [
    path('signin/<username>/<password>/', views.sign_in, name='signin'),
    path('login/<username>/<password>/', views.log_in, name='login'),
]

