from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# CHOICES = [
#     ('donator', 'Donator'),
#     ('deposit', 'Deposit'),
#     ('volunteer', 'Volunteer'),
# ]

class User(AbstractUser):
    # account_type = models.CharField(max_length=20, choices=CHOICES, default='donator')
    # active = models.BooleanField(default=False)
    is_volunteer = models.BooleanField(default=False)
    wilaya = models.IntegerField(default=0)
    baladiya = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.username
