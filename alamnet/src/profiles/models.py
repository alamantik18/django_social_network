from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils import timezone


class User(AbstractUser):
    """ Custom User model """
    GENDER_CHOICES = (
        ('Male', 'Male'), ('Female', 'Female')
    )

    phone = models.CharField(max_length=14, blank=True, null=True)
    avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)

    # Profile info fields
    bio = models.TextField(blank=True, null=True)
    github = models.CharField(max_length=1024, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=True, null=True)
    technologies = models.ManyToManyField('UserTechnology', related_name='users', blank=True, null=True)

    def __str__(self):
        return self.username


class UserTechnology(models.Model):
    """ Technologies for user """
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'User technology'
        verbose_name_plural = 'User technologies'
