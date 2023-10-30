from django.contrib import admin
from django.urls import path
from . import views
from .views import WelcomePageTemplateView, QuizCreateView, ResultDetailView, CarQuizBaseView, CarQuizPageTwoView, \
    CarQuizPageThreeView, CarQuizPageFourView, CarQuizPageFiveView, CarQuizPageSixView, CarQuizPageSevenView

urlpatterns = [
    path('', WelcomePageTemplateView.as_view(), name='quiz-welcome'),
    path('quiz/', QuizCreateView.as_view(), name='quiz'),
    path('quiz/2/<int:pk>', CarQuizPageTwoView.as_view(), name='quiz-2'),
    path('quiz/3/<int:pk>', CarQuizPageThreeView.as_view(), name='quiz-3'),
    path('quiz/4/<int:pk>', CarQuizPageFourView.as_view(), name='quiz-4'),
    path('quiz/5/<int:pk>', CarQuizPageFiveView.as_view(), name='quiz-5'),
    path('quiz/6/<int:pk>', CarQuizPageSixView.as_view(), name='quiz-6'),
    path('quiz/7/<int:pk>', CarQuizPageSevenView.as_view(), name='quiz-7'),
    path('result/<int:pk>', ResultDetailView.as_view(), name='quiz-result')
]