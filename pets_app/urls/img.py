
from django.urls import path
from pets_app.views import DogImgView, BreedImgView


urlpatterns = [
    path('', DogImgView.as_view(), name='dog-img'),
    path('breed/<str:image_id>/', BreedImgView.as_view(), name='breed-img')
]


