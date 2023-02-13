from rest_framework import serializers
from .models import Follower
from src.profiles.serializers import UserByFollowerSerializer

class ListFollowerSerializer(serializers.ModelSerializer):
    """ Serializer for output of user`s subscribers """
    subscriber = UserByFollowerSerializer(many=True, read_only=True)

    class Meta:
        model = Follower
        fields = ('subscriber', )
