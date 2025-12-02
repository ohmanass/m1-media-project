from django.urls import path

from . import views
from drf_spectacular.utils import extend_schema
from . import API_VERSION
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView

########################################## SWAGGER CRUCIAL CLASS ##########################################
"""
Class HealthCheckView
 Settings : 
    - APIView ( introduce by rest_frameworks.views )
""" 
class HealthCheckView(APIView):
    @extend_schema(
        summary="health check",
        description="Check if the API is alive or not",
        responses={200: PingSerializer},
        tags=["core"],
    )
    def get(self, request):
        return Response({"message": "pong"})
    
### URL PART ###
urlpatterns = [
    path("version", views.version, name="version"),
    path("ping", views.health_check, name="health_check"),
    path("health", HealthCheckView.as_view(), name="health_view"), # <- URL Swagger
]

