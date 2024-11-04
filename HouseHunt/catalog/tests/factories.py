from factory import fuzzy
import factory
from user.tests.factories import UserFactory

from ..models import Building

class BuildingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Building

    title = factory.Faker('word')
    price = fuzzy.FuzzyFloat(0.01, 100000)
    description = factory.Faker('paragraph')
    image_path = factory.django.ImageField(filename='building.jpg')
    user_id = factory.SubFactory(UserFactory)


