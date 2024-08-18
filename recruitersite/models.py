from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Vaccancy(models.Model):
    vaccancyid = models.IntegerField(blank=False,unique=True,primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    title = models.CharField(blank=True,max_length=100,unique=False)
    date_posted = models.DateTimeField()
    expiry_date = models.DateTimeField()
    recruiter = models.CharField(blank=True,max_length=100,unique=False)
    employmenttype = models.CharField(blank=True,max_length=100,unique=False)
    location = models.CharField(blank=True,max_length=100,unique=False)
    dutation = models.CharField(blank=True,max_length=100,unique=False)
    responsibilities = models.CharField(blank=True,max_length=500,unique=False)
    attributes = models.CharField(blank=True,max_length=300,unique=False)
    requirements = models.CharField(blank=True,max_length=500,unique=False)
    offer = models.CharField(blank=True,max_length=100,unique=False)
    def __str__(self):
        return self.user.username