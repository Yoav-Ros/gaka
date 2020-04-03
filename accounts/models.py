from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    xp = models.IntegerField(default=0)
    years_of_musical_experience = models.IntegerField(default=0)
    my_instruments = models.CharField(max_length=32, blank=True, null=True)
    short_description = models.CharField(max_length=280, blank=True, null=True)
    avatar = models.ImageField(upload_to='media/images', blank=True, null=True, default='media/images/toast.jpeg')
