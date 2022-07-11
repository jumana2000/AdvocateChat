from unicodedata import name
from django.db import models

# Create your models here.

class Register(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField(max_length=16)
    phone = models.IntegerField()
    password = models.CharField(max_length=10)