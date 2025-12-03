from rest_framework import serializers

"""
Classes Serializer 
"""

from django import forms

class PingSerializer(serializers.Serializer):
    message = serializers.CharField(
    )

class SerializerVersion(serializers.Serializer):
    version = serializers.CharField(
    )

class SerializerUpload(serializers.Serializer):
    file = serializers.FileField(
        required=True,
        help_text="File to upload (image or video)"
    )
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class UploadSerializer(serializers.Serializer):
    file = serializers.FileField()
    fileName = serializers.FileField()
    #fileName=serializers.CharField()