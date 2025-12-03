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

from .imagekit_manager import imagekit # <- imagekit.io import


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
    
######################################### IMAGEKIT.IO CRUCIAL CLASS #########################################
"""
Class UploadImageView
 Settings :
    - APIView ( introduce by rest_frameworks.views )
"""
class UploadImageView(APIView):
    # Post method to upload on imagekit.io
    def post(self, request):
        file = request.FILES.get('image')
        if not file:
            return Response({"error": "No file provided"}, status=400)
        # Upload the file using ImageKit
        res = imagekit.upload_file(
            file=file,
            file_name=file.name,
            options=None
        )
        # Returning PUBLIC URL & file ID
        return Response({
            "url": res.url,
            "file_id": res.file_id,
        })
    
    # Get method to avoid the warnings about get not found
    def get(self, request):
        return Response({"message": "Send a POST request with an image to upload"})
    
"""
Class UploadVideoView
 Settings :
    - APIView ( introduce by rest_frameworks.views )
"""
class UploadVideoView(APIView):
    # Post videos
    def post(self, request):
        file = request.FILES.get('video')
        if not file:
            return Response({"error": "No video file provided"}, status=400)

        # Checking correct transmission
        print(f"Received video: {file.name}, size: {file.size} bytes")

        # Upload to ImageKit
        res = imagekit.upload_file(
            file=file,
            file_name=file.name,
            options={
                "use_unique_file_name": False, 
            }
        )

        return Response({
            "url": res.url,
            "file_id": res.file_id,
            "original_name": res.name,
            "size": res.size
        })

    def get(self, request):
        return Response({"message": "Send a POST request with a video file to upload"})