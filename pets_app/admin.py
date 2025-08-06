from django.contrib import admin
from .models import Dog, Cat, Bird, ExoticAnimal, Owner

admin.site.register((Dog, Cat, Bird, ExoticAnimal, Owner))
