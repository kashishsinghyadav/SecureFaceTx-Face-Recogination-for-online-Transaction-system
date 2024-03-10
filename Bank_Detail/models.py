from django.db import models
from django.db.models.signals import post_save

class Creditmodel(models.Model):
    name_on_card=models.CharField(max_length=20)
    card_number=models.CharField(max_length=20)
    expiry_mm=models.CharField(max_length=5)
    cvv =models.CharField(max_length=5)

class Bankmodel(models.Model):
    account_holder=models.CharField(max_length=20)
    routing_number=models.CharField(max_length=5)
    account_type=models.CharField(max_length=10)
