from unittest.util import _MAX_LENGTH
from django.db import models

class services(models.Model):
    services_icon=models.CharField(max_length=50)
    services_title=models.CharField(max_length=50)
    services_des=models.TextField()
# Create your models here.
