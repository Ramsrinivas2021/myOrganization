
# Create your models here.
from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Instance(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    instance_id = models.CharField(max_length=100)

    # Other fields...

    def __str__(self):
        return self.instance_id