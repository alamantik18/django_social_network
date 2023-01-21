from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils import timezone

class User(AbstractUser):
    """ Custom User model """
    GENDER_CHOICES = (
        ('Male', 'Male'), ('Female', 'Female')
    )

    phone = models.CharField(max_length=14)
    avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True)
    middle_name = models.CharField(max_length=50)

    # Profile info fields
    bio = models.TextField(blank=True, null=True)
    github = models.CharField(max_length=1024, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=True, null=True)
