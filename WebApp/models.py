from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    name= models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    mobile= models.CharField(max_length=100)
    summary= models.TextField(max_length=1000)
    degree=models.CharField(max_length=100)
    school= models.CharField(max_length=100)
    university= models.CharField(max_length=100)
    experience= models.TextField(max_length=2000)
    skills= models.TextField(max_length=1000)

class Profile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username