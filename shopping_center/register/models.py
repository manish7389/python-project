from django.db import models
class register(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

# Create your models here.
