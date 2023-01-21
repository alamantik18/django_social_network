from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from .serializers import GetUserSerializer
from rest_framework import permissions
from django.shortcuts import render
from .models import User

class GetUserView(RetrieveAPIView):
    """ Output user info via api"""
    queryset = User.objects.all()
    serializer_class = GetUserSerializer

class UpdateUserView(UpdateAPIView):
    """ Update user via api"""
    serializer_class = GetUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
