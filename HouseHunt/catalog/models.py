from django.core.validators import MinValueValidator
from django.db import models
from user.models import CustomUser

# Create your models here.
class Building(models.Model):
    title = models.CharField(max_length=20, null=False, verbose_name='Название')
    price = models.FloatField(validators=[MinValueValidator(0.01)], null=False, verbose_name='Цена')
    description = models.TextField(null=False, verbose_name='Описание')
    image_path = models.ImageField(upload_to='images/', null=False, verbose_name='Изображение')
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.title

