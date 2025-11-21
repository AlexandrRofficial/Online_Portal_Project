from django.db import models

class Announcement(models.Model):
    title = models.CharField(max_length=100)
    important = models.BooleanField(default=True)
    #image = models.ImageField(upload_to='announcements/images/')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)