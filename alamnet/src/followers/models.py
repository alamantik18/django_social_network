from django.db import models

from alamnet.settings import AUTH_USER_MODEL


class Follower(models.Model):
    """ Subscriber model """
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author')
    subscriber = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followers')
