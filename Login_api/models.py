from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from  django.conf import settings 


# Create your models here.
class Login(models.Model):
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    f_name=models.CharField(max_length=255)
    l_name=models.CharField(max_length=255)
    number=models.IntegerField()

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def TokenCreate(sender,instance,created,**kwargs):
    if created:
        Token.objects.create(user=instance)
