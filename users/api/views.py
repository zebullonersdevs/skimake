# users/views.py
from rest_framework import generics
from users.models import CustomUser
from django.http import HttpResponse

from users.models import CustomUser, CustomUserProfile
from .serializers import UserSerializer


def home(request):
    return HttpResponse("welcome to skimake print api. append '/swagger' to the base url to view documentation")


class UserListView(generics.ListAPIView):
    queryset                = CustomUser.objects.all()
    serializer_class        = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field            = 'pk'
    queryset                = CustomUser.objects.all()
    serializer_class        = UserSerializer
    