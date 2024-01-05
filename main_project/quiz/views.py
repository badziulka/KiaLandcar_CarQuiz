from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from .forms import CarQuizBaseForm, CarQuizPageOneForm, CarQuizPageTwoForm, CarQuizPageThreeForm, CarQuizPageFourForm, \
    CarQuizPageFiveForm, CarQuizPageSixForm, CarQuizPageSevenForm
from .models import CarModel
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from urllib.parse import urlencode
from django.db.models import Q


class WelcomePageTemplateView(TemplateView):
    template_name = 'quiz/welcome.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Welcome'
        return context


class QuizCreateView(CreateView):
    model = CarModel
    form_class = CarQuizPageOneForm
    template_name = 'quiz/quiz_form.html'

    def get_success_url(self):
        return reverse_lazy('quiz-2', args=[self.object.id])


class CarQuizBaseView(UpdateView):
    model = CarModel
    template_name = 'quiz/quiz_form.html'
    success_url = None


class CarQuizPageTwoView(CarQuizBaseView):
    form_class = CarQuizPageTwoForm

    def get_success_url(self):
        return reverse_lazy('quiz-3', args=[self.object.id])


class CarQuizPageThreeView(CarQuizBaseView):
    form_class = CarQuizPageThreeForm

    def get_success_url(self):
        return reverse_lazy('quiz-4', args=[self.object.id])


class CarQuizPageFourView(CarQuizBaseView):
    form_class = CarQuizPageFourForm

    def get_success_url(self):
        return reverse_lazy('quiz-5', args=[self.object.id])


class CarQuizPageFiveView(CarQuizBaseView):
    form_class = CarQuizPageFiveForm

    def get_success_url(self):
        return reverse_lazy('quiz-6', args=[self.object.id])


class CarQuizPageSixView(CarQuizBaseView):
    form_class = CarQuizPageSixForm

    def get_success_url(self):
        return reverse_lazy('quiz-7', args=[self.object.id])


class CarQuizPageSevenView(CarQuizBaseView):
    form_class = CarQuizPageSevenForm

    def get_success_url(self):
        return reverse_lazy('quiz-result', args=[self.object.id])


class ResultDetailView(DetailView):
    model = CarModel
    template_name = 'quiz/result.html'

    def get_context_data(self, **kwargs):
        answers = {
            'person_count': self.object.person_count,
            'engine_type': self.object.engine_type,
            'road_type': self.object.road_type,
            'price': self.object.price,
            'preference': self.object.preference,
        }
        context = super().get_context_data(**kwargs)
        context['selected_cars'] = CarModel.get_car(answers)
        return context
