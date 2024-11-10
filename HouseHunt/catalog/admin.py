from django.contrib import admin
from django.template.defaultfilters import title

from .models import Building, TypeOfBuilding


# Register your models here.

def capitalize_title(self, request, queryset):
    for building in queryset:
        building.title = building.title.capitalize()
        building.save()

capitalize_title.short_description = 'Написать название с заглавной буквы'

class BuildingAdmin(admin.ModelAdmin):
    list_display = ('title', 'type_of_building', 'display_square', 'display_price', 'display_year_of_construction', 'price_for_m')
    ordering = ('year_of_construction',)
    list_filter = ('type_of_building',)
    search_fields = ('title', 'type_of_building__type_of_building')
    fieldsets = (
        ('Основная информация', {'fields': ('title', 'price', 'square')}),
        ('Дополнительня информация', {'fields': ('description', 'type_of_building', 'user_id')}),
    )
    actions = [capitalize_title]
    def display_square(self, obj):
        return obj.square
    display_square.short_description = 'Площадь'

    def display_price(self, obj):
        return obj.price
    display_price.short_description = 'Цена'

    def display_year_of_construction(self, obj):
        return obj.year_of_construction
    display_year_of_construction.short_description = 'Год постройки'

    def price_for_m(self, obj):
        return obj.price / obj.square
    price_for_m.short_description = 'Цена за м2'


admin.site.register(Building, BuildingAdmin)
