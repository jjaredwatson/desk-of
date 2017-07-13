from django.db import models
from django.contrib.auth.models import User

class Drink(models.Model):
    name = models.CharField(max_length=100)
    recipe = models.CharField(max_length=300)
    user = models.ForeignKey(User)

class Journal(models.Model):
    title = models.CharField(max_length=100)
    entry = models.CharField(max_length=2500)
    user = models.ForeignKey(User)

class Ipod(models.Model):
    album = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    track = models.CharField(max_length=100)
    user = models.ForeignKey(User)

def __str__(self):
		return self.name
