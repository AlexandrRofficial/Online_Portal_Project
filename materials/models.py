from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    extension = models.FileField(upload_to='materials/', blank=True, null=True)
