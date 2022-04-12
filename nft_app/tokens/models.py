from django.db import models


class Token(models.Model):
    unique_hash = models.CharField(max_length=255, unique=True, blank=True)
    tx_hash = models.CharField(max_length=255, unique=True, blank=True)
    media_url = models.URLField()
    owner = models.CharField(max_length=255, unique=True)
    random_string = models.CharField(max_length=20)
