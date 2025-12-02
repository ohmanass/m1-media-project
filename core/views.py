from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
import django
from core import API_VERSION  
# Swagger import
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema


# health_check & version routes
def health_check(request):
    data = {'message': 'pong'}
    return JsonResponse(data)

def version(request):
    return JsonResponse({
        "api_version": API_VERSION,
        "django_version": django.get_version(),
    })

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