from django.contrib import admin
from django.urls import path
from . import views
from .views import WelcomePageTemplateView, QuizCreateView, ResultDetailView, QuizPageTwoView, QuizPageThreeView, \
    QuizPageFourView, QuizPageFiveView, QuizPageSixView, QuizPageSevenView

urlpatterns = [
    path('', WelcomePageTemplateView.as_view(), name='quiz-welcome'),
    path('quiz/', QuizCreateView.as_view(), name='quiz'),
    path('quiz/2/<int:pk>', QuizPageTwoView.as_view(), name='quiz-2'),
    path('quiz/3/<int:pk>', QuizPageThreeView.as_view(), name='quiz-3'),
    path('quiz/4/<int:pk>', QuizPageFourView.as_view(), name='quiz-4'),
    path('quiz/5/<int:pk>', QuizPageFiveView.as_view(), name='quiz-5'),
    path('quiz/6/<int:pk>', QuizPageSixView.as_view(), name='quiz-6'),
    path('quiz/7/<int:pk>', QuizPageSevenView.as_view(), name='quiz-7'),
    path('result/<int:pk>', ResultDetailView.as_view(), name='quiz-result')
]