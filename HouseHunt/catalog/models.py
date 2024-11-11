from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from user.models import CustomUser


class TypeOfBuilding(models.Model):
    CHOICE_OF_TYPE = [
        ('apartment', 'Квартира'),
        ('house', 'Дом'),
        ('garage', 'Гараж'),
        ('commercial real estate', 'Коммерческая недвижимость'),
        ('non-residential real estate', 'Нежилая недвижимость'),
        ('none type', 'None type')
    ]
    type_of_building = models.CharField(max_length=50, choices=CHOICE_OF_TYPE, default='none type')

    def __str__(self):
        return self.type_of_building
# Create your models here.
class Building(models.Model):
    title = models.CharField(max_length=20, null=False, verbose_name='Название')
    type_of_building = models.ForeignKey(
        TypeOfBuilding, on_delete=models.CASCADE, null=False, verbose_name='Тип недвижимости')
    price = models.FloatField(validators=[MinValueValidator(0.01)], null=False, verbose_name='Цена')
    description = models.TextField(null=False, verbose_name='Описание')
    image_path = models.ImageField(upload_to='images/', null=False, verbose_name='Изображение')
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False)
    square = models.SmallIntegerField(validators=[MinValueValidator(0)], null=False)
    year_of_construction = models.SmallIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2024)],
                                                    null=False)
    def __str__(self):
        return (f"{self.title}, {self.type_of_building}, {self.square}, "
                f"{self.year_of_construction},{self.price}, {self.description[:20]},"
                f" {self.image_path}, {self.user_id}")





