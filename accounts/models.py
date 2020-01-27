from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_first_name = models.CharField(max_length=40, blank=False)
    user_last_name = models.CharField(max_length=40, blank=False)
    user_phone_number = models.CharField(max_length=20, blank=False)
    user_city = models.CharField(max_length=40, blank=False)
    user_street_address_1 = models.CharField(max_length=60, blank=False)
    user_street_address_2 = models.CharField(max_length=60, blank=False)
    user_county = models.CharField(max_length=40, blank=False)
    user_country = models.CharField(max_length=40, blank=False)
    user_postcode = models.CharField(max_length=20, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()