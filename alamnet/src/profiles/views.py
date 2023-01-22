from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .serializers import *
from django.shortcuts import render
from .models import User


class UserPublicView(ModelViewSet):
    """ Output of public profile """
    queryset = User.objects.all()
    serializer_class = GetPublicUserSerializer  # .serializers.py
    permission_classes = [permissions.AllowAny]


class UserView(ModelViewSet):
    """ Output user info via api """
    serializer_class = GetUserSerializer  # .serializers.py
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
