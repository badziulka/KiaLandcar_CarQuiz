from django.contrib import admin
from django.urls import path
from . import views
from .views import WelcomePageTemplateView, QuizCreateView, ResultTemplateView

urlpatterns = [
    path('', WelcomePageTemplateView.as_view(), name='quiz-welcome'),
    path('quiz/', QuizCreateView.as_view(), name='quiz'),
    path('result/', ResultTemplateView.as_view(), name='quiz-result')
]