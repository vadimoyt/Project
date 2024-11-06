# Generated by Django 5.1.2 on 2024-11-06 20:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_building_type_of_building'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='square',
            field=models.SmallIntegerField(default=None, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='building',
            name='year_of_construction',
            field=models.SmallIntegerField(default=None, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2024)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='typeofbuilding',
            name='type_of_building',
            field=models.CharField(choices=[('apartment', 'Квартира'), ('house', 'Дом'), ('garage', 'Гараж'), ('commercial real estate', 'Коммерческая недвижимость'), ('non-residential real estate', 'Нежилая недвижимость'), ('none type', 'None type')], default='none type', max_length=50),
        ),
    ]
