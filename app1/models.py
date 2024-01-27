from django.db import models

# Create your models here.from
from django.contrib.auth.models import User
class Profile(models.Model):
    UserName=models.OneToOneField(User,on_delete=models.CASCADE)
    adress=models.TextField()
    profile_pic=models.ImageField()

    
    