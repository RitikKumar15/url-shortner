from django.db import models

# Create your models here.
class UrlShortner(models.Model):
    long_url = models.CharField(max_length=1000)
    short_url = models.CharField(max_length=70, unique=True)