from rest_framework import serializers
from .models import Owner, Cat, Dog, Bird, ExoticAnimal

class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = '__all__'

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = '__all__'

class BirdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bird
        fields = '__all__'

class ExoticAnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExoticAnimal
        fields = '__all__'

class OwnerSerializer(serializers.ModelSerializer):
    cats = CatSerializer(many=True)
    dogs = DogSerializer(many=True)
    birds = BirdSerializer(many=True)
    exotic_animals = ExoticAnimalSerializer(many=True)

    class Meta:
        model = Owner
        fields = ['id', 'name', 'age', 'number_of_pets', 'cats', 'dogs', 'birds', 'exotic_animals']

