from django.db import models

class Users(models.Model):
    login = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=16)
    shalter_name = models.CharField(max_length=128, unique=True)
    address = models.CharField(max_length=128)
    email = models.CharField(max_length=64, unique=True)
    telephone = models.CharField(max_length=9, unique=True)

class Dogs(models.Model):
    dog_name = models.CharField(max_length=16, null=True)
    race = models.CharField(max_length=64)
    age = models.PositiveIntegerField(null=True)
    weight = models.FloatField()
    height = models.FloatField()
    description = models.CharField(max_length=1024)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

class Races(models.Model):
    race = models.CharField(max_length=64)