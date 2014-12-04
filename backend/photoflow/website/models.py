from django.db import models

# Create your models here.
class Website(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    photo_title = models.CharField(max_length=200)
    photo_description = models.CharField(max_length=300)