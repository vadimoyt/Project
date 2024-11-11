import factory
from factory import fuzzy

from user.tests.factories import UserFactory
from ..models import Building, TypeOfBuilding


class BuildingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Building

    title = factory.Faker('word')
    type_of_building = factory.LazyAttribute(
        lambda o: TypeOfBuilding.objects.get(id=2)
    )

    price = fuzzy.FuzzyFloat(0.01, 100000)
    description = factory.Faker('paragraph')
    image_path = factory.django.ImageField(filename='building.jpg')
    user_id = factory.SubFactory(UserFactory)
    square = fuzzy.FuzzyInteger(1, 200)
    year_of_construction = fuzzy.FuzzyInteger(1900,2024)


