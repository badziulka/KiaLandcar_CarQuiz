from django.db import models


class CarModel(models.Model):

    person_count = models.CharField(max_length=32)# blank=True, default='person_count_2_4')
    engine_type = models.CharField(max_length=74)
    road_type = models.CharField(max_length=74)
    price = models.CharField(max_length=48)
    preference = models.CharField(max_length=74)

    PERSON_COUNT_CHOICES = [('person_count_1', 'Tylko ja'), ('person_count_2', '2'), ('person_count_3_4', '3-4'),
                            ('person_count_5_7', '5-7')]

    ENGINE_TYPE_CHOICES = [('engine_type_petrol', 'benzyna'), ('engine_type_diesel', 'diesel'),
                           ('engine_type_hybrid', 'hybryda'), ('engine_type_electric', 'elektryczny')]

    ROAD_TYPE_CHOICES = [('road_type_city', 'tylko miasto'), ('road_type_mixed', 'cykl mieszany'),
                         ('road_type_route', 'głównie trasy'), ('road_type_mostly_city', 'głównie miasto, czasami trasy')]

    PRICE_CHOICES = [('price_100', '0-100 tysięcy'), ('price_100_150', '100-150 tysięcy'),
                     ('price_150_200', '150-200 tysięcy'), ('price_200', 'więcej niż 200 tysięcy')]

    PREFERENCE_CHOICES = [('preference_simple', 'prostotę'), ('preference_comfort', 'komfort'),
                          ('preference_mul_config', 'dużą możliwość konfiguracji'), ('preference_technology', 'nowinki technologiczne')]




# # Create your models here.
# Picanto(liczbaosob=1, 2, paliwo=benzyna, trasa=miasto, kwota=100tys)
# Xceed()
#
# CarModel
# name = 'Picanto'
# paliwo = field
# trasa =
# kwota =


