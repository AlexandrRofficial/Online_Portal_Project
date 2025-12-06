from django.db import models
from django.contrib.auth.models import User

class profile(models.Model):
    Name = models.CharField(max_length=23)
    description = models.CharField(max_length=500)


class post(models.Model):
    post = models.CharField(max_length=200)



# Create your models here.
