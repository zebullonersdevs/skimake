# users/serializers.py
from rest_framework import serializers 
from users.models import CustomUser, CustomUserProfile, CustomUserWallet
from drf_writable_nested.serializers import WritableNestedModelSerializer
from drf_writable_nested.mixins import  UniqueFieldsMixin, NestedUpdateMixin


class UserProfileSerializer(UniqueFieldsMixin, NestedUpdateMixin, serializers.ModelSerializer):
    class Meta:
        model               = CustomUserProfile
        fields              = '__all__'

class UserWalletSerializer(UniqueFieldsMixin, NestedUpdateMixin, serializers.ModelSerializer):
    class Meta:
        model               = CustomUserWallet
        fields              = '__all__'

class UserSerializer(UniqueFieldsMixin, NestedUpdateMixin, serializers.ModelSerializer):
    customuserprofile       = UserProfileSerializer()
    customuserwallet        = UserWalletSerializer()
    class Meta:
        model               = CustomUser
        fields              = ('__all__')

