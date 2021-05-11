from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Passengers(models.Model):
    user = models.OneToOneField(
        User, blank=True, null=True, on_delete=models.SET_DEFAULT, default=None)


    phone_number = models.CharField(max_length=40, default=None)
    
    

    def __str__(self):
        return self.user


