from hashlib import blake2b
from random import choices
from secrets import choice
from statistics import mode
from django.db import models

# Create your models here.


usertype= (
    ('Customer','Customer'),
    ('Cook','Cook')
    )


class UserRegister(models.Model):
    name  = models.CharField(max_length=20)
    address  = models.CharField(max_length=20)
    phone_no = models.IntegerField()
    
    role = models.CharField(max_length=20,choices=usertype)

    def __str__(self):
        return self.role




class CookRegister(models.Model):
    user = models.ForeignKey(UserRegister,on_delete=models.CASCADE, null=True,blank=True,)
    country = models.CharField(max_length=20)
    speciality = models.CharField(max_length=20)
    
    
   



class CustomerRegister(models.Model):
    user = models.ForeignKey(UserRegister,on_delete=models.CASCADE, null=True,blank=True,)
    job = models.CharField(max_length=20)
    pncode = models.IntegerField()
    
 