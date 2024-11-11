from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from .models import Building, TypeOfBuilding


class BuildingForm(forms.ModelForm):
    CHOICE_OF_TYPE = [
        ('apartment', 'Квартира'),
        ('house', 'Дом'),
        ('garage', 'Гараж'),
        ('commercial real estate', 'Коммерческая недвижимость'),
        ('non-residential real estate', 'Нежилая недвижимость'),
        ('none type', 'None type')
    ]
    title = forms.CharField(max_length=30, required=True, label='Название')
    type_of_building = forms.ModelChoiceField(label='Тип недвижимости', queryset=TypeOfBuilding.objects.all())
    price = forms.FloatField(validators=[MinValueValidator(0)], required=True, label='Цена')
    year_of_construction = forms.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2024)],
        required=True, label='Год постройки')
    square = forms.IntegerField(validators=[MinValueValidator(0)], required=True, label='Площадь')
    description = forms.CharField(max_length=250, required=True, label='Описание')
    image_path = forms.ImageField(required=True, label='Фото')
    class Meta:
        model = Building
        fields = ['title', 'type_of_building', 'price', 'year_of_construction', 'square','description', 'image_path']