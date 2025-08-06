from django.db import models
from django.contrib.auth.models import AbstractUser

class PetOwner(AbstractUser):
    email = 'email'
    REQUIRED_FIELDS = []
    

class Owner(models.Model):
    name = models.CharField(max_length=100)
    age = models.BigIntegerField()
    number_of_pets = models.BigIntegerField()
    
    
class ExoticAnimal(models.Model):
    region_of_origin = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    age = models.BigIntegerField()
    type_of_animal = models.CharField(max_length=100)
    vaccinated = models.BooleanField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='exotic_animals')

class Bird(models.Model):
    name = models.CharField(max_length=100)
    age = models.BigIntegerField()
    vaccinated = models.BooleanField()
    description = models.TextField()
    species = models.CharField(max_length=100)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='birds')
    
    
class Cat(models.Model):
    breed = models.CharField(max_length=100)
    age = models.BigIntegerField()
    vaccinated = models.BooleanField()
    description = models.TextField()
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='cats')
    
    
class Dog(models.Model):
    age = models.BigIntegerField()
    name = models.CharField(max_length=100)
    vaccinated = models.BooleanField()
    breed = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='dogs')
    
    