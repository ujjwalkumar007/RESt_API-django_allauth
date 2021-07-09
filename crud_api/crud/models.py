from django.db import models

# requirements for generating tokens.
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token



class Course(models.Model):
    #class for Course model
    name = models.CharField(null=False, max_length=50)
    author = models.CharField(null=False, max_length=100)
    date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    users_enrolled = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "course"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    #Function for generating token each time a new user register
    if created:
        Token.objects.create(user=instance)


class Wishlist(models.Model):
    #class for Wishlist model
    user = models.CharField(null=False, max_length=50) #user name
    course = models.CharField(null=False, max_length=100) #wishlist course

    def __str__(self):
        return self.user

    class Meta:
        db_table = "wishlist"
