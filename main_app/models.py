from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=100)
    recipe = models.CharField(max_length=300)

class Journal(models.Model):
    title = models.CharField(max_length=100)
    entry = models.CharField(max_length=500)

def __str__(self):
		return self.name
