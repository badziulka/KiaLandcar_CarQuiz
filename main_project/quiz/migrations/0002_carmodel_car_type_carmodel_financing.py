# Generated by Django 4.2.6 on 2023-10-19 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='car_type',
            field=models.CharField(default='car_type_suv', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carmodel',
            name='financing',
            field=models.CharField(default='financing_cash', max_length=48),
            preserve_default=False,
        ),
    ]
