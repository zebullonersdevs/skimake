# users/serializers.py
from rest_framework import serializers
from users.models import CustomUser, CustomUserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model               = CustomUser
        fields              = ('__all__')

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model               = CustomUserProfile
        fields              = '__all__'