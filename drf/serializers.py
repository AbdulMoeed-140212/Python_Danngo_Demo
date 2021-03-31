from rest_framework import serializers
from drf.models import UserDemo

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model= UserDemo
        exclude = ("created_at", "updated_at",)