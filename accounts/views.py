from django.http import JsonResponse
from accounts.models import Student
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET'])
def sign_in(request, username, password):
    """
    Stores the values into Stident Model and returuns the status
    """
    if request.method == 'GET':
        
        if username and password:
            
            if not Student.objects.filter(username=username):
                Student.objects.create(
                    username=username,
                    password=password
                )
                return Response({'status': 'True',})
            
            return Response({'status': 'False',})
        
        return Response({'status': 'False',})


# 127.0.0.1:8000/signin/alimov/easy_password


@api_view(['GET'])
def log_in(request, username, password):
    """
    User exists in DB? 
    """
    if request.method == 'GET':
        
        if Student.objects.filter(username=username, password=password):
            return Response({'status': 'True',})
        return Response({'status': 'False',})