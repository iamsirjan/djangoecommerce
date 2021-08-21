from rest_framework import generics
from rest_framework.response import Response
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import login
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import get_object_or_404

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


class ProfileAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):

        return Response(ProfileSerializer(request.user).data)


class AnswerApi(generics.ListAPIView, generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = answer.objects.all()
    serializer_class = AnswerSerializer


class QuizApi(generics.ListAPIView, generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = quiz.objects.all()
    serializer_class = QuizSerializer


class QuizgetApi(generics.ListAPIView, generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = quiz.objects.all()
    serializer_class = QuizgetSerializer


class QuizApidelete(generics.UpdateAPIView, generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = quiz.objects.all()
    serializer_class = QuizSerializer
    lookup_field = 'id'


class ResultAPi(generics.ListAPIView, generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = result.objects.all()
    serializer_class = obtainresultSerializer
