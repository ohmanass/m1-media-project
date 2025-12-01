from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
import django

###def index(request):
 ###   return HttpResponse("Hello, world. You're at the polls index.")

def health_check(request):
    data = {'message': 'pong'}
    return JsonResponse(data)

def version(request):
    return JsonResponse({"Django version :": django.get_version()})