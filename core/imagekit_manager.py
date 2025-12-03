# import
from imagekitio import ImageKit
from django.conf import settings

# Create an ImageKit client instance for uploading videos, url ...
imagekit = ImageKit(
    public_key=settings.IMAGEKIT_PUBLIC_KEY,
    private_key=settings.IMAGEKIT_PRIVATE_KEY,
    url_endpoint=settings.IMAGEKIT_URL_ENDPOINT,
)