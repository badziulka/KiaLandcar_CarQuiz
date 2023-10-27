from django.contrib import admin
from django.urls import path
from . import views
from .views import WelcomePageTemplateView, QuizCreateView, ResultDetailView, QuizPageTwoView

urlpatterns = [
    path('', WelcomePageTemplateView.as_view(), name='quiz-welcome'),
    path('quiz/', QuizCreateView.as_view(), name='quiz'),
    path('quiz/2/<int:pk>', QuizPageTwoView.as_view(), name='quiz-2'),
    path('result/<int:pk>', ResultDetailView.as_view(), name='quiz-result')
]