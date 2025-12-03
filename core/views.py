import logging
import django

from django.http import JsonResponse
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from .serializers import PingSerializer

from media.services import upload_file

logger = logging.getLogger(__name__)

# ============================================ BASIC ROUTES ============================================

def health_check(request):
    return JsonResponse({"message": "pong"})


def version(request):
    return JsonResponse({
        "api_version": settings.API_VERSION,
        "django_version": django.get_version(),
    })

# ====================================== HEALTH CHECK VIEW (Swagger) ======================================
"""
class HealthCheckView
    - Settings : APIView ( imported w//rest_framework.views)
    - Goal : View the HelathCheckView w//swagger
"""
class HealthCheckView(APIView):
    @extend_schema(
        summary="Health Check",
        description="Returns pong if API is alive",
        responses={200: PingSerializer},
        tags=["core"]
    )
    def get(self, request):
        return Response({"message": "pong"})

# ============================== UPLOAD FILE VIEW to ImageKit.io with REST API ==============================
"""
class UploadFileView
    - Settings : APIView ( imported w//rest_framework.views)
    - Goal : Upload files on IMAGEKIT.IO thanks to API 
"""
class UploadFileView(APIView):
    @extend_schema(
        summary="Upload a file to ImageKit.io",
        tags=["core"],
        request={
            "multipart/form-data": {
                "type": "object",
                "properties": {
                    "file": {"type": "string", "format": "binary"},
                },
                "required": ["file"]
            }
        },
        responses={200: dict},
    )
    def post(self, request):
        file = request.FILES.get("file")
        if not file:
            return Response({"error": "No file provided"}, status=400)

        result = upload_file(file)
        return Response(result)