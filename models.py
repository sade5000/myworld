from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils import timezone
from .manager import abusers
from django.conf import settings

class CustomUser(AbstractBaseUser,PermissionsMixin):
    email= models.EmailField(_("email address"), unique=True)
    #password=models.CharField()
    
    is_staff= models.BooleanField(default=False)
    is_active= models.BooleanField(default=True)
    #Differenciate Users by Priviledges
    is_service= models.BooleanField(default=False)
    is_supplier= models.BooleanField(default=False)
    is_vendor= models.BooleanField(default=False)
    is_costumer= models.BooleanField(default=False)  
    ####End   
    #Credentials
    
    date_joined= models.DateTimeField(default=timezone.now)
    firstname=models.CharField(max_length= 40, null= True)
    lastname=models.CharField(max_length= 40, null= True)
    profile_pic= models.ImageField(default='company_logo.png',upload_to='BASE_DIR/"mystatic"',null=True)
    
    USERNAME_FIELD= "email"
    REQUIRED_FIELDS= []
    
    objects= abusers()
    
    def __str__(self):
        return self.email

class Profile(models.Model):
    user= models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_img= models.ImageField(default='company_logo.png',upload_to='BASE_DIR/"mystatic"',null=True)
    dob= models.DateField(default=timezone.now)
    first_line_address= models.CharField(max_length= 50 , null=True)
    second_line_address= models.CharField(max_length= 50, null= True)
    postcode= models.CharField(max_length = 10, null=True)
    def __str__(self):
        return f'{self.user.email}   {self.user.firstname} {self.user.lastname} Profile'
class Shop(models.Model):
    user=models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    shop_name=models.CharField(max_length=30, null=True)
    shop_legal_no=models.CharField(max_length=30, null=True)
    shop_img= models.ImageField(default='company_logo.png',upload_to='BASE_DIR/"mystatic"',null=True)
    shop_sales=models.FloatField()
    def __str__(self):
        return f'{self.user} {self.id} {self.shop_name} Shop'
    
    

    