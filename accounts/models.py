from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to="media/profiles", blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
