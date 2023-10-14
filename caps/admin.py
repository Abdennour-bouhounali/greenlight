from django.contrib import admin

from .models import Donation, Deposit, Acceptation

# Register your models here.

admin.site.register(Donation)
admin.site.register(Deposit)
admin.site.register(Acceptation)
