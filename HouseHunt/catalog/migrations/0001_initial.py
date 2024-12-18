# Generated by Django 5.1.2 on 2024-10-30 18:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Название')),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.01)], verbose_name='Цена')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image_path', models.ImageField(upload_to='images/', verbose_name='Изображение')),
            ],
        ),
    ]
