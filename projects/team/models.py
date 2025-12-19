from django.db import models
from championship.models import Championship

# Create your models here.



class Team(models.Model):

    name= models.CharField(max_length=200)
    championship = models.ForeignKey(Championship, on_delete=models.CASCADE, related_name='teams')

    def __str__(self):
        return self.name
    