from rest_framework import serializers
from .models import User

class GetUserSerializer(serializers.ModelSerializer):
    """ Display the profile of the same user """

    class Meta:
        model = User
        exclude = ('password', 'is_active', 'is_staff', 'last_login', 'is_superuser', 'groups', 'user_permissions')

class GetPublicUserSerializer(serializers.ModelSerializer):
    """ Output public info about user """

    class Meta:
        model = User
        exclude = ('password', 'is_active', 'is_staff', 'last_login',
                   'is_superuser', 'groups', 'email', 'user_permissions')
