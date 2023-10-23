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


class ResultTemplateView(TemplateView):
    template_name = 'quiz/result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Results'

        answers = {
            'car_type': self.request.POST.get('car_type'),
            'person_count': self.request.POST.get('person_count'),
            'engine_type': self.request.POST.get('engine_type'),
            'road_type': self.request.POST.get('road_type'),
            'price': self.request.POST.get('price'),
            'preference': self.request.POST.get('preference'),
            'financing': self.request.POST.get('financing'),
        }

        selected_cars = CarModel.get_car(answers)

        context['selected_cars'] = selected_cars


        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context)



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
