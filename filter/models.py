# models.py
from django.db import models

class Species(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Sex(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Breed(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name