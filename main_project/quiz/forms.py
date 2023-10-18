from django import forms
from .models import CarModel
from django.forms import ModelForm


class CarQuizForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'

    car_type = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=[
            ('suv', 'Suv'),
            ('combi', 'kombi'),
            ('cov', 'crossover'),
            ('hatchback', 'hatchback')

        ],
        label='Jakim rodzajem samochodu jeździsz obecnie?'
    )

    person_count = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CarModel.PERSON_COUNT_CHOICES,
        label='Ile osób jeździ najczęściej z tobą w samochodzie?'
    )

    engine_type = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CarModel.ENGINE_TYPE_CHOICES,
        label='Jaki typ silnika chciałbyś mieć w swoim samochodzie?'
    )

    road_type = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CarModel.ROAD_TYPE_CHOICES,
        label='Gdzie najwięcej jeździsz?'
    )

    price = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CarModel.PRICE_CHOICES,
        label='Do jakiej kwoty chciałbyś kupić samochód?'
    )

    preferences = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CarModel.PREFERENCE_CHOICES,
        label='Na co zwrócisz uwagę przy wyborze kolejnego pojazdu?'
    )

    financing = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=[
            ('cash', 'gotówka/przelew'),
            ('credit', 'kredyt'),
            ('leasing', 'leasing'),
            ('renting', 'najem')
        ],
        label='Jaką formę finansowania bierzesz pod uwagę?'
    )

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