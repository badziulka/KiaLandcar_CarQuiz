from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from .forms import CarQuizForm
from .models import CarModel
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView



class WelcomePageTemplateView(TemplateView):
    template_name = 'quiz/welcome.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Welcome'
        return context


class QuizCreateView(CreateView):
    model = CarModel
    form_class = CarQuizForm
    template_name = 'quiz/quiz_form.html'
    success_url = '/result/'

    def form_valid(self, form):
        car_type = form.cleaned_data['car_type']
        person_count = form.cleaned_data['person_count']
        engine_type = form.cleaned_data['engine_type']
        road_type = form.cleaned_data['road_type']
        price = form.cleaned_data['price']
        preferences = form.cleaned_data['preferences']
        financing = form.cleaned_data['financing']


        car_model = CarModel(
            car_type=car_type,
            person_count=person_count,
            engine_type=engine_type,
            road_type=road_type,
            price=price,
            preferences=preferences,
            financing=financing
        )
        car_model.save()

        return redirect('quiz-result')


class ResultTemplateView(TemplateView):
    template_name = 'quiz/result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Results'
        return context
#
# def quiz(request):
#     if request.method == 'POST':
#         form = CarQuizForm(request.POST)
#
#         if form.is_valid():
#             # request.session['quiz_answers'] = form.cleaned_data
#             return redirect('quiz-welcome')
#     else:
#         form = CarQuizForm()
#     return render(request, 'quiz/quiz_form.html', {'form': form})
