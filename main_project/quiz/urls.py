from django.contrib import admin
from django.urls import path
from . import views
from .views import WelcomePageTemplateView, QuizCreateView, ResultDetailView

urlpatterns = [
    path('', WelcomePageTemplateView.as_view(), name='quiz-welcome'),
    path('quiz/', QuizCreateView.as_view(), name='quiz'),
    path('result/', ResultDetailView.as_view(), name='quiz-result')
]