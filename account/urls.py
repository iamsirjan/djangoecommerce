from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import *

urlpatterns = [
    path('register/', RegisterUser.as_view()),
    path('currentuser/', ProfileAPI.as_view()),
    path('quiz-question/', QuizApi.as_view()),
    path('get-quiz-question/', QuizgetApi.as_view()),
    path('question-delete/<id>/', QuizApidelete.as_view()),
    path('result/', ResultAPi.as_view()),



    path('quiz-answer/', AnswerApi.as_view()),


    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
