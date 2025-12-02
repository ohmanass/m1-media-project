from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
import django
from core import API_VERSION  

# health_check & version routes
def health_check(request):
    data = {'message': 'pong'}
    return JsonResponse(data)

def version(request):
    return JsonResponse({
        "api_version": API_VERSION,
        "django_version": django.get_version(),
    })