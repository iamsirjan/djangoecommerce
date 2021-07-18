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
            email=validated_data['email'], mobile=validated_data['mobile'])
        users.set_password(validated_data['password'])
        users.save()
        return users


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        data.update({'user': self.user.email})
        data.update({'id': self.user.id})
        data.update({'mobile': self.user.mobile})

        return data
