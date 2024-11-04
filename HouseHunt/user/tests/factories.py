import factory

from ..models import CustomUser


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = CustomUser

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = factory.PostGenerationMethodCall('set_password', 'defaultpassword')



