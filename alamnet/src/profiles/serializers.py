from rest_framework import serializers
from .models import User

class GetUserSerializer(serializers.ModelSerializer):
    """ Output info about user """

    class Meta:
        model = User
        exclude = ('password', 'is_active', 'is_staff', 'last_login', 'is_superuser', 'groups')
