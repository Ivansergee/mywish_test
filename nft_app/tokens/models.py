from django.db import models


class Token(models.Model):
    unique_hash = models.CharField(max_length=20, unique=True)
    tx_hash = models.CharField(max_length=255, blank=True)
    media_url = models.URLField(max_length=2000)
    owner = models.CharField(max_length=255)

    def __str__(self):
        return self.unique_hash
