from rest_framework import serializers

"""
Class 
"""
class PingSerializer(serializers.Serializer):
    message = serializers.CharField(
    )

class SerializerVersion(serializers.Serializer):
    version = serializers.CharField(
    )