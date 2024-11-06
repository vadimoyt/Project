from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOISES = [
        ('buyer', 'Buyer'),
        ('owner', 'Owner')
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOISES, default='Buyer')