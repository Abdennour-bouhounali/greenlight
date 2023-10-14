from django.db import models

from accounts.models import User

# Create your models here.

class Donation(models.Model):
    donator = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    wilaya = models.IntegerField()
    baladiya = models.IntegerField()
    wait_for_vol = models.BooleanField(default=False)
    donated = models.BooleanField(default=False)
    collected = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.quantity} from {self.donator.username}'


class Deposit(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    wilaya = models.IntegerField()
    baladiya = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.capacity} from {self.owner.username}'


class Acceptation(models.Model):
    volunteer = models.ForeignKey(User, on_delete=models.CASCADE)
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE)
    donation_accepted = models.BooleanField(default=False)
    donation_rejected = models.BooleanField(default=False)
    deposit = models.ForeignKey(Deposit, on_delete=models.CASCADE, null=True)
    deposit_accepted = models.BooleanField(default=False)
    deposit_rejected = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.donation} to {self.deposit}'
