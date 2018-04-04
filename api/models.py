from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# Create your models here.


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Route(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Coordinates(models.Model):
    route = models.ForeignKey(Route, related_name='route', blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    easting = models.CharField(max_length=10)
    northing = models.CharField(max_length=10)
    serial = models.IntegerField()
    control = models.BooleanField(default=0)

    def __str__(self):
        return self.name
