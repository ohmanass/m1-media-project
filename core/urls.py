from django.urls import path
from .views import HealthCheckView, UploadFileView

urlpatterns = [
    path("health/", HealthCheckView.as_view(), name="health-check"),
    path("upload_file/", UploadFileView.as_view(), name="upload-file"),
]