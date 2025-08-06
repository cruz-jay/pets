from django.urls import path
from pets_app.views import (
    AllOwnersView,
    SingleOwnerView,
    OwnerSpecificPetView,
)

urlpatterns = [
    path('', AllOwnersView.as_view(), name='all-owners'),
    path('<int:id>/', SingleOwnerView.as_view(), name='single-owner'),
    path('<int:id>/pets/<int:pet_id>/', OwnerSpecificPetView.as_view(), name='owner-specific-pet'),
]
