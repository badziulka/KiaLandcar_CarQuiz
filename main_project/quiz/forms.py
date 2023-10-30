from django import forms
from .models import CarModel
from django.forms import ModelForm


class CarQuizBaseForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = ()


class CarQuizPageOneForm(CarQuizBaseForm):
    car_type = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CarModel.CarType.choices,
        label='Jakim rodzajem samochodu jeździsz obecnie?'
    )

    class Meta(CarQuizBaseForm.Meta):
        fields = ('car_type',)


class CarQuizPageTwoForm(CarQuizBaseForm):
    person_count = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices= CarModel.PersonCount.choices,
        label='Ile osób jeździ najczęściej z tobą w samochodzie?'
    )

    class Meta(CarQuizBaseForm.Meta):
        fields = ('person_count',)


class CarQuizPageThreeForm(CarQuizBaseForm):
    engine_type = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices = CarModel.EngineType.choices,
        label='Jaki typ silnika chciałbyś mieć w swoim samochodzie?'
    )

    class Meta(CarQuizBaseForm.Meta):
        fields = ('engine_type',)


class CarQuizPageFourForm(CarQuizBaseForm):
    road_type = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices = CarModel.RoadType.choices,
        label='Gdzie najwięcej jeździsz?'
    )

    class Meta(CarQuizBaseForm.Meta):
        fields = ('road_type',)


class CarQuizPageFiveForm(CarQuizBaseForm):
    price = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices= CarModel.Price.choices,
        label='Do jakiej kwoty chciałbyś kupić samochód?'
    )

    class Meta(CarQuizBaseForm.Meta):
        fields = ('price',)


class CarQuizPageSixForm(CarQuizBaseForm):
    preference = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices= CarModel.Preference.choices,
        label='Na co zwrócisz uwagę przy wyborze kolejnego pojazdu?'
    )

    class Meta(CarQuizBaseForm.Meta):
        fields = ('preference',)


class CarQuizPageSevenForm(CarQuizBaseForm):
    financing = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices= CarModel.Financing.choices,
        label='Jaką formę finansowania bierzesz pod uwagę?'
    )

    class Meta(CarQuizBaseForm.Meta):
        fields = ('financing',)


#
# class CarQuizForm(forms.ModelForm):
#     class Meta:
#         model = CarModel
#         fields = ('car_type',)
#         widgets = {
#             'car_type': forms.RadioSelect(attrs={'choices': CarModel.CarType.choices})
#         }
#         labels = {'car_type': 'Jakim rodzajem samochodu jeździsz obecnie?'}
#
#
# class CarQuizPageTwoForm(forms.ModelForm):
#     class Meta:
#         model = CarModel
#         fields = ('person_count',)
#         widgets = {
#             'person_count': forms.RadioSelect(attrs={'choices': CarModel.PersonCount.choices})
#         }
#         labels = {'person_count': 'Ile osób jeździ najczęściej z tobą w samochodzie?'}
#
#
# class CarQuizPageThreeForm(forms.ModelForm):
#     class Meta:
#         model = CarModel
#         fields = ('engine_type',)
#         widgets = {
#             'engine_type': forms.RadioSelect(attrs={'choices': CarModel.EngineType.choices})
#         }
#         labels = {'engine_type': 'Jaki typ silnika chciałbyś mieć w swoim samochodzie?'}
#
#
# class CarQuizPageFourForm(forms.ModelForm):
#     class Meta:
#         model = CarModel
#         fields = ('road_type',)
#         widgets = {
#             'road_type': forms.RadioSelect(attrs={'choices': CarModel.RoadType.choices})
#         }
#         labels = {'road_type': 'Gdzie najwięcej jeździsz?'}
#
#
# class CarQuizPageFiveForm(forms.ModelForm):
#     class Meta:
#         model = CarModel
#         fields = ('price',)
#         widgets = {
#             'price': forms.RadioSelect(attrs={'choices': CarModel.Price.choices})
#         }
#         labels = {'price': 'Do jakiej kwoty chciałbyś kupić samochód?'}
#
#
# class CarQuizPageSixForm(forms.ModelForm):
#     class Meta:
#         model = CarModel
#         fields = ('preference',)
#         widgets = {
#             'preference': forms.RadioSelect(attrs={'choices': CarModel.Preference.choices})
#         }
#         labels = {'preference': 'Na co zwrócisz uwagę przy wyborze kolejnego pojazdu?'}
#
#
# class CarQuizPageSevenForm(forms.ModelForm):
#     class Meta:
#         model = CarModel
#         fields = ('financing',)
#         widgets = {
#             'financing': forms.RadioSelect(attrs={'choices': CarModel.Financing.choices})
#         }
#         labels = {'financing': 'Jaką formę finansowania bierzesz pod uwagę?'}




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