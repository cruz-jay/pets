"""
URL configuration for Pets_Two project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def root_view(request):
    
    home = """
    <h1>Links</h1>
    
    <h3> DB Sourced Stuff </h3> 
    <ul>
        <li><a href="/admin/">Admin</a></li>
        <li><a href="/api/v1/pets/">Pets</a> </li>
        <li><a href="/api/v1/owners/">Owners</a> </li>
    </ul>
    
    
    <h3> 3rd Party APIs </h3> 

    <ul>
        <li><a href="/api/dog-img/">One Dog IMG</a></li>
        <li><a href="/api/dog-img/breed/">Breed</a></li>
        <li><a href="/api/dog-img/breed/">All Cat Breeds</a></li>

    </ul>
    
    """
    return HttpResponse(home)

urlpatterns = [
    path('', root_view, name='root'),
    path('admin/', admin.site.urls),
    path('api/v1/pets/', include('pets_app.urls.pets')),
    path('api/v1/owners/', include('pets_app.urls.owners')),
    path('api/dog-img/', include('pets_app.urls.img'))
]
