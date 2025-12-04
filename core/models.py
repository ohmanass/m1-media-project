from django.db import models
import uuid # To have unique ID and not 1234...

"""
class MediaFile
    - Settings : models.Model
    - Goal : Stock media informations in PSQL Table
"""
class MediaFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file_name = models.TextField()
    file_type = models.CharField(
        max_length=50,
        choices=[("image", "Image"), ("video", "Video"), ("other", "Other")],
        default="other"
    )
    url = models.URLField()
    size = models.BigIntegerField(unique=True, primary_key=False, serialize=True)
    created_at = models.DateTimeField(auto_now_add=True)
    meta_data = models.BooleanField()