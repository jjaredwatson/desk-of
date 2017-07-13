from django.db import models
from django.core.urlresolvers import reverse

class Drink(models.Model):
    name = models.CharField(max_length=100)
    recipe = models.CharField(max_length=300)

class Journal(models.Model):
    title = models.CharField(max_length=100)
    entry = models.CharField(max_length=2500)

class Ipod(models.Model):
    album = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    track = models.CharField(max_length=100)

def __str__(self):
		return self.name

def get_absolute_url(self):
        return reverse('drink_edit', kwargs={'pk': self.pk})
