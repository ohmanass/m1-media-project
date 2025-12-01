from django.urls import path

from . import views

urlpatterns = [
    path("version", views.version, name="version"),
    path("ping", views.health_check, name="health_check"),
]
