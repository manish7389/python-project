import email
from django.db import models

class contactinqury(models.Model):
    name = models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    massage = models.TextField()

# Create your models here.
