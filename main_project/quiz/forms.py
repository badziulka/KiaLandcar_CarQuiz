from django import forms
from .models import CarModel
from django.forms import ModelForm


class CarQuizForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = ('car_type',)
        widgets = {
            'car_type': forms.RadioSelect(attrs={'label': 'testowy label', 'choices': CarModel.CarType.choices})
        }

class CarQuizPageTwoForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = ('person_count',)
        widgets = {
            'person_count': forms.RadioSelect(attrs={'label': 'testowy label', 'choices': CarModel.PersonCount.choices})
        }
        labels = {'person_count': 'Ile osób jeździ najczęściej z tobą w samochodzie?'}


    # car_type = forms.ChoiceField(
    #     widget=forms.RadioSelect,
    #     choices=CarModel.CarType.choices,
    #     label='Jakim rodzajem samochodu jeździsz obecnie?'
    # )
    #
    # person_count = forms.ChoiceField(
    #     widget=forms.RadioSelect,
    #     choices=CarModel.PersonCount.choices,
    #     label='Ile osób jeździ najczęściej z tobą w samochodzie?'
    # )
    #
    # engine_type = forms.ChoiceField(
    #     widget=forms.RadioSelect,
    #     choices=CarModel.EngineType.choices,
    #     label='Jaki typ silnika chciałbyś mieć w swoim samochodzie?'
    # )
    #
    # road_type = forms.ChoiceField(
    #     widget=forms.RadioSelect,
    #     choices=CarModel.RoadType.choices,
    #     label='Gdzie najwięcej jeździsz?'
    # )
    #
    # price = forms.ChoiceField(
    #     widget=forms.RadioSelect,
    #     choices=CarModel.Price.choices,
    #     label='Do jakiej kwoty chciałbyś kupić samochód?'
    # )
    #
    # preference = forms.ChoiceField(
    #     widget=forms.RadioSelect,
    #     choices=CarModel.Preference.choices,
    #     label='Na co zwrócisz uwagę przy wyborze kolejnego pojazdu?'
    # )
    #
    # financing = forms.ChoiceField(
    #     widget=forms.RadioSelect,
    #     choices=CarModel.Financing.choices,
    #     label='Jaką formę finansowania bierzesz pod uwagę?'
    # )

# class CarQuizForm(forms.Form):
#     car_type = forms.ChoiceField(
#         label='Jakim rodzajem samochodu jeździsz obecnie?',
#         choices=[
#             ('suv', 'Suv'),
#             ('combi', 'kombi'),
#             ('cov', 'crossover'),
#             ('hatchback', 'hatchback')
#
#         ],
#         widget=forms.RadioSelect
#     )
#
#     person_count = forms.ChoiceField(
#         choices=CarModel.PERSON_COUNT_CHOICES,
#         widget=forms.RadioSelect,
#         label='Ile osób jeździ najczęściej z tobą w samochodzie?'
#     )
#
#     engine_type = forms.ChoiceField(
#         choices=CarModel.ENGINE_TYPE_CHOICES,
#         widget=forms.RadioSelect,
#         label='Jaki typ silnika chciałbyś mieć w swoim samochodzie?'
#     )
#
#     road_type = forms.ChoiceField(
#         choices=CarModel.ROAD_TYPE_CHOICES,
#         widget=forms.RadioSelect,
#         label='Gdzie najwięcej jeździsz?'
#     )
#
#     price = forms.ChoiceField(
#         choices=CarModel.PRICE_CHOICES,
#         widget=forms.RadioSelect,
#         label='Do jakiej kwoty chciałbyś kupić samochód?'
#     )
#
#     preferences = forms.ChoiceField(
#         choices=CarModel.PREFERENCE_CHOICES,
#         widget=forms.RadioSelect,
#         label='Na co zwrócisz uwagę przy wyborze kolejnego pojazdu?'
#     )
#
#     financing = forms.ChoiceField(
#         label='Jaką formę finansowania bierzesz pod uwagę?',
#         choices=[
#             ('cash', 'gotówka/przelew'),
#             ('credit', 'kredyt'),
#             ('leasing', 'leasing'),
#             ('renting', 'najem')
#         ],
#         widget=forms.RadioSelect
#     )