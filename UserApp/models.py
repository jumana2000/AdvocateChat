
from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Register(models.Model):
    name = models.CharField(max_length=10,null=True,blank=False)
    email = models.EmailField(max_length=20,null=True,blank=False)
    phone = models.IntegerField(default=0)
    password = models.CharField(max_length=10,null=True,blank=False)
    status = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class LRegister(models.Model):
    name = models.CharField(max_length=10,null=True,blank=False)
    email = models.EmailField(max_length=20,null=True,blank=False)
    phone = models.IntegerField(default=0)
    enrollment_no = models.CharField(max_length=10,null=True,blank=False)
    password = models.CharField(max_length=10,null=True,blank=False)
    status = models.IntegerField(default=0)
    law = models.CharField(max_length=20,null=True,blank=False)
    lawyer_image = models.ImageField(upload_to='lawyer_image',default=0)

    def __str__(self):
        return self.name