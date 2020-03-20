# users/views.py
from rest_framework import generics
from users.models import CustomUser

from users.models import CustomUser, CustomUserProfile
from .serializers import UserSerializer

class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    