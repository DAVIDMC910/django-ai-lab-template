from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    
    path("", include("tienda.urls", namespace="tienda")),

    # nueva app de la actividad
    path("academico/", include("academico.urls", namespace="academico")),
]