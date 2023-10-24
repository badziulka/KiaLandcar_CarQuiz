from django.db import models
from django.db.models import Q


class CarModel(models.Model):
    car_type = models.CharField(max_length=32)
    person_count = models.CharField(max_length=32)  # blank=True, default='person_count_2_4')
    engine_type = models.CharField(max_length=74)
    road_type = models.CharField(max_length=74)
    price = models.CharField(max_length=48)
    preference = models.CharField(max_length=74)
    financing = models.CharField(max_length=48)

    CAR_TYPE_CHOICES = [('car_type_suv', 'suv'), ('car_type_combi', 'kombi'), ('car_type_cov', 'crossover'),
                        ('car_type_hatchback', 'hatchback')]

    PERSON_COUNT_CHOICES = [('person_count_1', 'Tylko ja'), ('person_count_2', '2'), ('person_count_3_4', '3-4'),
                            ('person_count_5_7', '5-7')]

    ENGINE_TYPE_CHOICES = [('engine_type_petrol', 'benzyna'), ('engine_type_diesel', 'diesel'),
                           ('engine_type_hybrid', 'hybryda'), ('engine_type_electric', 'elektryczny')]

    ROAD_TYPE_CHOICES = [('road_type_city', 'tylko miasto'), ('road_type_mixed', 'cykl mieszany'),
                         ('road_type_route', 'głównie trasy'),
                         ('road_type_mostly_city', 'głównie miasto, czasami trasy')]

    PRICE_CHOICES = [('price_100', '0-100 tysięcy'), ('price_100_150', '100-150 tysięcy'),
                     ('price_150_200', '150-200 tysięcy'), ('price_200', 'więcej niż 200 tysięcy')]

    PREFERENCE_CHOICES = [('preference_simple', 'prostotę'), ('preference_comfort', 'komfort'),
                          ('preference_mul_config', 'dużą możliwość konfiguracji'),
                          ('preference_technology', 'nowinki technologiczne')]

    FINANCING_CHOICES = [('financing_cash', 'gotówka/przelew'), ('financing_credit', 'kredyt'),
                         ('financing_leasing', 'leasing'), ('financing_renting', 'najem')]


    @staticmethod
    def get_car(answers):
        conditions = {
            'picanto_stonic': (
                    Q(person_count__in=['person_count_1', 'person_count_2']) & Q(engine_type='engine_type_petrol')
                    & Q(road_type='road_type_city') & Q(price='price_100') & Q(preference='preference_simple')
            ),

            'ceed': (
                     Q(person_count__in=['person_count_2', 'person_count_3_4'])
                     & Q(engine_type__in=['engine_type_petrol','engine_type_hybrid'])
                     & Q(road_type__in=['road_type_mixed', 'road_type_route', 'road_type_mostly_city'])
                     & Q(price='price_100_150') & Q(preference='preference_simple')
            ),

            'sportage': (
                    Q(person_count='person_count_3_4') & Q(engine_type__in=['engine_type_hybrid', 'engine_type_petrol'])
                    & Q(road_type__in=['road_type_mixed', 'road_type_route', 'road_type_mostly_city'])
                    & Q(price__in=['price_100_150', 'price_150_200']) & Q(preference__in=['preference_comfort', 'preference_mul_config'])
            ),

            'proceed': (
                    Q(person_count='person_count_3_4') & Q(engine_type='engine_type_petrol')
                    & Q(road_type__in=['road_type_mixed', 'road_type_route', 'road_type_mostly_city'])
                    & Q(price='price_100_150') & Q(preference='preference_simple')
            ),

            'niro': (
                    Q(person_count='person_count_3_4') & Q(engine_type='engine_type_hybrid') & Q(road_type='road_type_city')
                    & Q(price='price_100_150') & Q(preference='preference_comfort')
            ),

            'niro_ev': (
                    Q(person_count='person_count_3_4') & Q(engine_type='engine_type_electric') & Q(road_type='road_type_city')
                    & Q(price='price_200') & Q(preference='preference_comfort')
            ),
            'ev6': (
                    Q(person_count='person_count_3_4') & Q(engine_type='engine_type_electric')
                    & Q(road_type__in=['road_type_mixed', 'road_type_mostly_city']) & Q(price='price_200')
                    & Q(preference__in=['preference_comfort', 'preference_mul_config', 'preference_technology'])
            ),

            'xceed': (
                    Q(person_count='person_count_3_4') & Q(engine_type__in=['engine_type_petrol', 'engine_type_hybrid'])
                    & Q(road_type__in=['road_type_mixed', 'road_type_route', 'road_type_mostly_city'])
                    & Q(price='price_100_150') & Q(preference='preference_simple')
            ),

            'sorento': (
                    Q(person_count='person_count_5_7') & Q(engine_type__in=['engine_type_hybrid', 'engine_type_diesel'])
                    & Q(road_type__in=['road_type_mixed', 'road_type_route', 'road_type_mostly_city'])
                    & Q(price='price_200') & Q(preference__in=['preference_comfort', 'preference_mul_config', 'preference_technology'])
            ),

            'ev9': (
                    Q(person_count='person_count_5_7') & Q(engine_type='engine_type_electric')
                    & Q(road_type__in=['road_type_mixed', 'road_type_mostly_city']) & Q(price='price_200')
                    & Q(preference__in=['preference_comfort', 'preference_mul_config', 'preference_technology'])
            )
        }

        selected_cars = []

        for car_name, condition in conditions.items():
            print(car_name, condition)
            if CarModel.objects.filter(condition).exists():
                selected_cars.append(car_name)

        return selected_cars

        # {{ object.get_car }}


# # Create your models here.
# Picanto(liczbaosob=1, 2, paliwo=benzyna, trasa=miasto, kwota=100tys)
# Xceed()
#
# CarModel
# name = 'Picanto'
# paliwo = field
# trasa =
# kwota =
