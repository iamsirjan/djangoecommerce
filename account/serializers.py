from django.db.models import fields
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate, login
from rest_framework.response import Response


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = user
        fields = ['email', 'password', 'mobile']

    def create(self, validated_data):
        users = user.objects.create(
            email=validated_data['email'], mobile=validated_data['mobile'], password=validated_data['password'])
        # users.set_password(validated_data['password'])
        users.save()
        return users


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        data.update({'email': self.user.email})
        data.update({'id': self.user.id})
        data.update({'mobile': self.user.mobile})

        return data


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['id', 'email', 'mobile']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = answer
        fields = ['id', 'answer', 'status']


class QuizSerializer(serializers.ModelSerializer):
    answers = serializers.PrimaryKeyRelatedField(
        queryset=answer.objects.all(), many=True)

    class Meta:
        model = quiz
        fields = ['question', 'answers']


class QuizgetSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = quiz
        fields = ['id', 'question', 'answers']


class obtainresultSerializer(serializers.ModelSerializer):
    user = ProfileSerializer(many=True)

    class Meta:
        model = result
        fields = ['id', 'obtainmarks', 'user']
