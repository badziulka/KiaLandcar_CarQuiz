from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from .forms import CarQuizForm
from .models import CarModel
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
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
    form_class = CarQuizForm
    template_name = 'quiz/quiz_form.html'

    def get_success_url(self):
        # params = {
        #     # 'car_type': self.request.POST.get('car_type'),
        #     'person_count': self.request.POST.get('person_count'),
        #     'engine_type': self.request.POST.get('engine_type'),
        #     'road_type': self.request.POST.get('road_type'),
        #     'price': self.request.POST.get('price'),
        #     'preference': self.request.POST.get('preference'),
        #     # 'financing': self.request.POST.get('financing'),
        # }
        # query_string = urlencode(params)
        return reverse_lazy('quiz-result', args=[self.object.id])# + f'?{query_string}'


class ResultDetailView(DetailView):
    model = CarModel
    template_name = 'quiz/result.html'
    # context_object_name = 'selected_cars'


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
