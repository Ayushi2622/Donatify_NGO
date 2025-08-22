from django.db import models
from django.utils import timezone

# Create your models here.
###Contact Model
class Contact(models.Model):
    name=models.CharField(max_length=50,null=False)     #num=False is default in Django#
    email=models.EmailField(max_length=50,null=False) 
    phone=models.CharField(max_length=13,null=False) 
    query=models.TextField(default="")
    date=models.DateField(default=timezone.now)

# Feedback Model
class FeedBack(models.Model):
    name=models.CharField(max_length=50,null=False)     #num=False is default in Django#
    email=models.EmailField(max_length=50,null=False,primary_key=True) 
    rating=models.CharField(max_length=5,null=False) 
    remarks=models.TextField(default="")
    date=models.DateField(default=timezone.now)

# User
class User(models.Model):
    name=models.CharField(max_length=50,null=False)     #num=False is default in Django#
    email=models.EmailField(max_length=50,null=False,primary_key=True) 
    password=models.CharField(max_length=50,null=False)
    phone=models.CharField(max_length=13,null=False) 
    profile_pic=models.FileField(upload_to="user_pic/",default="")
    date=models.DateField(default=timezone.now)

# Campaign 
class Campaign(models.Model):
    title=models.CharField(max_length=50,null=False)     
    description=models.TextField(default="")
    pic=models.FileField(upload_to="camp_pic/",default="")
    from_date=models.CharField(max_length=10,null=False) 
    to_date=models.CharField(max_length=10,null=False)
    venue=models.TextField(default="")

# Donation
class Donation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.CharField(max_length=10,default="")
    aadhaar = models.FileField(max_length=10,default="")
    transaction_id = models.CharField(max_length=10,default="")
    date = models.DateField(default=timezone.now)
    paymentstatus= models.CharField(default="Pending",max_length=10)




