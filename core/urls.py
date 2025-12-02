from django.urls import path
from . import views
from drf_spectacular.utils import extend_schema
from .views import HealthCheckView

urlpatterns = [
    path("version", views.version, name="version"),
    path("ping", views.health_check, name="health_check"),
    path("health", HealthCheckView.as_view(), name="health_view"), # <- URL Swagger
]