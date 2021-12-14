from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import timedelta

# Create your models here.
from django.template.defaulttags import now


class User(AbstractUser):
    image = models.ImageField(upload_to='users_image', blank=True)
    age = models.PositiveIntegerField(default=18)

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expores = models.DateField(auto_now=True, blank=True, null=True)


def is_activation_key_expores(self):
    if now() <= self.activation_key_expores == timedelta(hours=48):
        return False
