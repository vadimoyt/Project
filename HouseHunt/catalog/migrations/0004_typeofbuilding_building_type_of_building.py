# Generated by Django 5.1.2 on 2024-11-06 19:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_building_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeOfBuilding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_building', models.CharField(choices=[('apartment', 'Apartment'), ('house', 'House'), ('garage', 'Garage'), ('commercial real estate', 'Commercial real estate'), ('non-residential real estate', 'Non-residential real estate'), ('none type', 'None type')], default='None type', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='building',
            name='type_of_building',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='catalog.typeofbuilding'),
            preserve_default=False,
        ),
    ]