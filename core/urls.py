from django.urls import path
from . import views
from .views import HealthCheckView, UploadImageView, UploadVideoView

urlpatterns = [
    path("version", views.version, name="version"),
    path("ping", views.health_check, name="health_check"),
    path("health", HealthCheckView.as_view(), name="health_view"),    # <- URL Swagger
    path("upimg", UploadImageView.as_view(), name="uploaded_image"), # <- IMAGEKIT.IO path ( upload img )
    path("upvid", UploadVideoView.as_view(), name="upload_video"),   # <- Upload videos on IMAGEKIT.IO
]