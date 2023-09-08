from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    payment_id = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    # username = models.CharField(max_length=255)
    # email = models.CharField(max_length=255, unique=True) 
    # phone_number = models.CharField(max_length=20, null=True)
    # first_name = models.CharField(max_length=255)
    # last_name = models.CharField(max_length=255)
    # address = models.PROTECT(max_length=255)