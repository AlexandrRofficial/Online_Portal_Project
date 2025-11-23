from django.db import models

class profile(models.Model):
    Name = models.CharField(max_length=23)
    Description = models.CharField(max_length=500)

# Create your models here.
