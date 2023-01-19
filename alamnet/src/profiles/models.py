from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """ Custom User model """

    first_login = models.DateTimeField(verbose_name='first_login', null=True)
    phone = models.CharField(max_length=14)
    avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True)
    middle_name = models.CharField(max_length=50)
