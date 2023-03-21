from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Clients(models.Model):
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField(max_length=255)
    client_phone = PhoneNumberField(max_length=15)
