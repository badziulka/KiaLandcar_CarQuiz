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

