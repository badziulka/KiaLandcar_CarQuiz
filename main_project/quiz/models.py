from django.db import models
from django.db.models import Q


class CarModel(models.Model):
    class CarType(models.TextChoices):
        SUV = 'car_type_suv', 'suv'
        COMBI = 'car_type_combi', 'kombi'
        COV = 'car_type_cov', 'crossover'
        HATCHBACK = 'car_type_hatchback', 'hatchback'

    car_type = models.CharField(
        max_length=32,
        choices=CarType.choices,
        default=CarType.SUV
    )

    class PersonCount(models.TextChoices):
        PERSON_COUNT_1 = 'person_count_1', 'Tylko ja'
        PERSON_COUNT_2 = 'person_count_2', '2'
        PERSON_COUNT_3_4 = 'person_count_3_4', '3-4'
        PERSON_COUNT_5_7 = 'person_count_5_7', '5-7'

    person_count=models.CharField(
        max_length=32,
        choices=PersonCount.choices,
        default=PersonCount.PERSON_COUNT_3_4
    )

    class EngineType(models.TextChoices):
        petrol = 'engine_type_petrol', 'benzyna'
        diesel = 'engine_type_diesel', 'diesel'
        hybrid = 'engine_type_hybrid', 'hybryda'
        electric = 'engine_type_electric', 'elektryczny'

    engine_type=models.CharField(
        max_length=74,
        choices=EngineType.choices,
        default=EngineType.diesel
    )

    class RoadType(models.TextChoices):
        city = 'road_type_city', 'tylko miasto'
        mixed = 'road_type_mixed', 'cykl mieszany'
        route = 'road_type_route', 'głównie trasy'
        mostly_city = 'road_type_mostly_city', 'głównie miasto, czasami trasy'

    road_type= models.CharField(
        max_length=74,
        choices=RoadType.choices,
        default=RoadType.mixed
    )

    class Price(models.TextChoices):
        price_100 = 'price_100', '0-100 tysięcy'
        price_100_150 = 'price_100_150', '100-150 tysięcy'
        price_150_200 = 'price_150_200', '150-200 tysięcy'
        price_200 = 'price_200', 'więcej niż 200 tysięcy'

    price= models.CharField(
        max_length=48,
        choices=Price.choices,
        default=Price.price_150_200
    )

    class Preference(models.TextChoices):
        simple = 'preference_simple', 'prostotę'
        comfort = 'preference_comfort', 'komfort'
        mul_config = 'preference_mul_config', 'dużą możliwość konfiguracji'
        technology = 'preference_technology', 'nowinki technologiczne'

    preference = models.CharField(
        max_length=74,
        choices=Preference.choices,
        default=Preference.comfort
    )

    class Financing(models.TextChoices):
        cash = 'financing_cash', 'gotówka/przelew'
        credit = 'financing_credit', 'kredyt'
        leasing = 'financing_leasing', 'leasing'
        renting = 'financing_renting', 'najem'

    financing = models.CharField(
        max_length=48,
        choices=Financing.choices,
        default=Financing.cash
    )


        # car_type = models.CharField(max_length=32, choices=)# choices=(('a', 'A'), ('b', 'B')))#, choices=)
    # person_count = models.CharField(max_length=32)  # blank=True, default='person_count_2_4')
    # engine_type = models.CharField(max_length=74)
    # road_type = models.CharField(max_length=74)
    # price = models.CharField(max_length=48)
    # preference = models.CharField(max_length=74)
    # financing = models.CharField(max_length=48)

    # result = models.CharField(max_length=24)

    # CAR_TYPE_CHOICES = [('car_type_suv', 'suv'), ('car_type_combi', 'kombi'), ('car_type_cov', 'crossover'),
    #                     ('car_type_hatchback', 'hatchback')]

    # PERSON_COUNT_CHOICES = [('person_count_1', 'Tylko ja'), ('person_count_2', '2'), ('person_count_3_4', '3-4'),
    #                         ('person_count_5_7', '5-7')]

    # ENGINE_TYPE_CHOICES = [('engine_type_petrol', 'benzyna'), ('engine_type_diesel', 'diesel'),
    #                        ('engine_type_hybrid', 'hybryda'), ('engine_type_electric', 'elektryczny')]

    # ROAD_TYPE_CHOICES = [('road_type_city', 'tylko miasto'), ('road_type_mixed', 'cykl mieszany'),
    #                      ('road_type_route', 'głównie trasy'),
    #                      ('road_type_mostly_city', 'głównie miasto, czasami trasy')]
    #
    # PRICE_CHOICES = [('price_100', '0-100 tysięcy'), ('price_100_150', '100-150 tysięcy'),
    #                  ('price_150_200', '150-200 tysięcy'), ('price_200', 'więcej niż 200 tysięcy')]
    #
    # PREFERENCE_CHOICES = [('preference_simple', 'prostotę'), ('preference_comfort', 'komfort'),
    #                       ('preference_mul_config', 'dużą możliwość konfiguracji'),
    #                       ('preference_technology', 'nowinki technologiczne')]
    #
    # FINANCING_CHOICES = [('financing_cash', 'gotówka/przelew'), ('financing_credit', 'kredyt'),
    #                      ('financing_leasing', 'leasing'), ('financing_renting', 'najem')]


    @staticmethod
    def get_car(answers):
        selected_cars = []
        conditions = {
            'picanto_stonic': (
            Q(person_count='person_count_1') | Q(person_count='person_count_2') & Q(engine_type='engine_type_petrol')
            & Q(road_type='road_type_city') & Q(price='price_100') & Q(preference='preference_simple')
            ),

            'ceed': (
                Q(person_count='person_count_2') | Q(person_count='person_count_3_4') & Q(engine_type='engine_type_petrol')
                | Q(engine_type='engine_type_hybrid') & Q(road_type='road_type_mixed') | Q(road_type='road_type_route')
                | Q(road_type='road_type_mostly_city') & Q(price='price_100_150') & Q(preference='preference_simple')
            ),

            'sportage': (
                Q(person_count='person_count_3_4') & Q(engine_type='engine_type_hybrid') | Q(engine_type='engine_type_petrol')
                & Q(road_type='road_type_mixed') | Q(road_type='road_type_route') | Q(road_type='road_type_mostly_city')
                & Q(price='price_100_150') | Q(price='price_150_200') & Q(preference='preference_comfort')
                | Q(preference='preference_mul_config')
            ),

            'proceed': (
                Q(person_count='person_count_3_4') & Q(engine_type='engine_type_petrol')
                & Q(road_type='road_type_mixed') | Q(road_type='road_type_route') | Q(road_type='road_type_mostly_city')
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
                Q(person_count='person_count_3_4') & Q(engine_type='engine_type_electric') & Q(road_type='road_type_mixed')
                | Q(road_type='road_type_mostly_city') & Q(price='price_200') & Q(preference='preference_comfort')
                | Q(preference='preference_mul_config') | Q(preference='preference_technology')

            ),

            'xceed': (
                Q(person_count='person_count_3_4') & Q(engine_type='engine_type_petrol') | Q(engine_type='engine_type_hybrid')
                & Q(road_type='road_type_mixed') | Q(road_type='road_type_route') | Q(road_type='road_type_mostly_city')
                & Q(price='price_100_150') & Q(preference='preference_simple')

            ),

            'sorento': (
                Q(person_count='person_count_5_7') & Q(engine_type='engine_type_hybrid') | Q(engine_type='engine_type_diesel')
                & Q(road_type='road_type_mixed') | Q(road_type='road_type_route') | Q(road_type='road_type_mostly_city')
                & Q(price='price_200') & Q(preference='preference_comfort') | Q(preference='preference_mul_config')
                | Q(preference='preference_technology')
            ),

            'ev9': (
                Q(person_count='person_count_5_7') & Q(engine_type='engine_type_electric') & Q(road_type='road_type_mixed')
                | Q(road_type='road_type_mostly_city') & Q(price='price_200') & Q(preference='preference_comfort')
                | Q(preference='preference_mul_config') | Q(preference='preference_technology')

            )
        }

        car_mapping = {
            'picanto_stonic': 'picanto_stonic.png',
            'ceed': 'ceed.png',
            'sportage': 'sportage.png',
            'proceed': 'proceed.png',
            'niro': 'niro.png',
            'niro_ev': 'niro_ev.png',
            'ev6': 'ev6.png',
            'xceed': 'xceed.png',
            'sorento': 'sorento.png',
            'ev9': 'ev9.png',
        }

        car_names = {
            'picanto_stonic': 'Picanto oraz Stonic',
            'ceed': 'Ceed',
            'sportage': 'Sportage',
            'proceed': 'Proceed',
            'niro': 'Niro',
            'niro_ev': 'Niro EV',
            'ev6': 'EV6',
            'xceed': 'XCeed',
            'sorento': 'Sorento',
            'ev9': 'EV9',
        }

        for car_name, condition in conditions.items():
            if CarModel.objects.filter(condition, **answers).exists():
                selected_cars.append((car_names.get(car_name, 'Brak modelu'), car_mapping.get(car_name, 'default.png')))

        return selected_cars





# # Create your models here.
# Picanto(liczbaosob=1, 2, paliwo=benzyna, trasa=miasto, kwota=100tys)
# Xceed()
#
# CarModel
# name = 'Picanto'
# paliwo = field
# trasa =
# kwota =
