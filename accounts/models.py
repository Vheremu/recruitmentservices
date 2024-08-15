from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phonenumber = models.CharField(blank=True,max_length=50,unique=False)
    profile_pic = models.ImageField(upload_to='static/profile_pics',blank=True)

    def __str__(self):
        return self.user.username