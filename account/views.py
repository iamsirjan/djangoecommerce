from rest_framework import generics
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import login
from rest_framework_simplejwt.views import TokenObtainPairView

from . import models
from . import serializers
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.


class RegisterUser(APIView):
    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if not serializer.is_valid():
                return Response({"status": 403, 'errors': serializer.errors,  'message': 'something went wrong'})
            serializer.save()
            users = user.objects.get(email=serializer.data['email'])
            refresh = RefreshToken.for_user(users)
            return Response({"status": 200, 'payload': serializer.data, 'refresh': str(refresh),
                             'access': str(refresh.access_token), 'message': 'registered'})
        except Exception as e:
            print(e)

            return Response({'status': 404, 'error': 'something went wrong'})


class CustomTokenObtainPairView(TokenObtainPairView):
    # Replace the serializer with your custom
    serializer_class = CustomTokenObtainPairSerializer
    token_obtain_pair = TokenObtainPairView.as_view()
