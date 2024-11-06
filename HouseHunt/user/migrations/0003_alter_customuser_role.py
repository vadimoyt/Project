# Generated by Django 5.1.2 on 2024-11-06 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('buyer', 'Buyer'), ('owner', 'Owner')], default='Buyer', max_length=10),
        ),
    ]