from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    age = serializers.IntegerField()
    email = serializers.EmailField()
    created_at = serializers.DateTimeField()
