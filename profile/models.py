from django.db import models

class profile(models.Model):
    name = models.CharField(max_length=23)
    description = models.CharField(max_length=500)

# Create your models here.
