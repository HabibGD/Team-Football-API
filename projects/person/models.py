from django.db import models
from team.models import Team

# Create your models here.

class Person(models.Model):

    fullname = models.CharField(max_length=200)
    sexe = models.CharField(max_length=100)
    teams = models.ManyToManyField(Team, related_name='persons')


    def __str__(self):
        return self.fullname