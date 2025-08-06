from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Owner, Cat, Dog, Bird, ExoticAnimal
from .serializers import (
    CatSerializer, DogSerializer, BirdSerializer,
    ExoticAnimalSerializer, OwnerSerializer
)
import requests

#---------------------------------#
from django.conf import settings  # 
#---------------------------------#


## 1
class AllPetsView(APIView):
    def get(self, request):
        cats = CatSerializer(Cat.objects.all(), many=True).data
        dogs = DogSerializer(Dog.objects.all(), many=True).data
        birds = BirdSerializer(Bird.objects.all(), many=True).data
        exotics = ExoticAnimalSerializer(ExoticAnimal.objects.all(), many=True).data

        return Response({
            "cats": cats,
            "dogs": dogs,
            "birds": birds,
            "exotic_animals": exotics
        })


## 2
class PetsByTypeView(APIView):
    def get(self, request, type_of_animal):
        type_of_animal = type_of_animal.lower()
        
        if type_of_animal == "cat":
            data = CatSerializer(Cat.objects.all(), many=True).data
        elif type_of_animal == "dog":
            data = DogSerializer(Dog.objects.all(), many=True).data
        elif type_of_animal == "bird":
            data = BirdSerializer(Bird.objects.all(), many=True).data
        elif type_of_animal == "exotic":
            data = ExoticAnimalSerializer(ExoticAnimal.objects.all(), many=True).data
        else:
            return Response({"error, bad  animal type"}, status=400)

        return Response(data)

# 3 ?!?!?!
class SinglePetByTypeAndIDView(APIView):
    def get(self, request, type_of_pet, id):
        type_of_pet = type_of_pet.lower()

        if type_of_pet == "cat":
            pet = get_object_or_404(Cat, id=id)
            data = CatSerializer(pet).data
        elif type_of_pet == "dog":
            pet = get_object_or_404(Dog, id=id)
            data = DogSerializer(pet).data
        elif type_of_pet == "bird":
            pet = get_object_or_404(Bird, id=id)
            data = BirdSerializer(pet).data
        elif type_of_pet == "exotic":
            pet = get_object_or_404(ExoticAnimal, id=id)
            data = ExoticAnimalSerializer(pet).data
        else:
            return Response({"error": "Invalid !!!!!fe3f 3e"}, status=400)

        return Response(data)



# 4
class AllOwnersView(APIView):
    def get(self, request):
        owners = Owner.objects.all()
        data = []
        for owner in owners:
            pet_names = (
                [cat.name for cat in owner.cats.all()] +
                [dog.name for dog in owner.dogs.all()] +
                [bird.name for bird in owner.birds.all()] +
                [ex.name for ex in owner.exotic_animals.all()]
            )
            data.append({
                "id": owner.id,
                "name": owner.name,
                "pet_names": pet_names
            })
        return Response(data)



# 5 
class SingleOwnerView(APIView):
    def get(self, request, id):
        owner = get_object_or_404(Owner, id=id)
        data = OwnerSerializer(owner).data
        return Response(data)


# 6
class OwnerSpecificPetView(APIView):
    def get(self, request, id, pet_id):
        owner = get_object_or_404(Owner, id=id)

        for model, serializer in [
            (Cat, CatSerializer),
            (Dog, DogSerializer),
            (Bird, BirdSerializer),
            (ExoticAnimal, ExoticAnimalSerializer)
        ]:
            try:
                pet = model.objects.get(id=pet_id, owner=owner)
                return Response(serializer(pet).data)
            except model.DoesNotExist:
                continue

        return Response({"error"}, status=404)




class DogImgView(APIView):
    def get(self, request):

        url = 'https://api.thedogapi.com/v1/images/search'
        headers = {
            "x-api-key": settings.DOG_API_KEY
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            
            # if data:
            #     img_url = data[0].get("url", None)
            #     return Response({"image_url": img_url})
            
            
            return Response(data)
        except requests.RequestException:
            return Response(status=500)
        
        
class BreedImgView(APIView):
    def get(self, request, image_id):
        url = f"https://api.thedogapi.com/v1/images/{image_id}/breeds"
        headers = {
            "x-api-key": settings.DOG_API_KEY
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            
            return Response(data)
        
        except requests.RequestException:
            return Response(status=500)
        

            
