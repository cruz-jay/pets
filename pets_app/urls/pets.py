from django.urls import path, register_converter
from pets_app.views import (
    AllPetsView,
    PetsByTypeView,
    SinglePetByTypeAndIDView,
)

class AnimalTypeConverter:
    regex = 'cat|dog|bird|exotic'

    def to_python(self, value):
        return value.lower()

    def to_url(self, value):
        return value

register_converter(AnimalTypeConverter, 'animal_type')

urlpatterns = [
    path('', AllPetsView.as_view(), name='all-pets'),
    path('<str:type_of_animal>/', PetsByTypeView.as_view(), name='pets-by-type'),
    path('<animal_type:type_of_pet>/pet/<int:id>/', SinglePetByTypeAndIDView.as_view(), name='single-pet-by-type-and-id'),
]

# http://127.0.0.1:8000/api/v1/pets/cat/pet/1/