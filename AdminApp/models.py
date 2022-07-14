from django.db import models

# Create your models here.

class Law(models.Model):
    name = models.CharField(max_length=20,null=True,blank=False)
    law_image = models.ImageField(upload_to='law_image')
    
    def __str__(self):
        return self.name