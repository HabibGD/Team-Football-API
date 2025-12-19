from django.db import models

# Create your models here.

class Championship(models.Model):

    champ_name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.champ_name