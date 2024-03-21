from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager



# Create your models here.
#class abusers(models.Model):
class abusers(BaseUserManager):
    """
    Custom user model manager :
        - email is unique identifier instead auth by username

    Args:
        models (_type_): _description_
    """
    def create_user(self,email,password,**extra_fields):
        """
        Create and save user with a given email and pass

        Args:
            email (_type_): _description_
            password (_type_): _description_
        """
        
        if not email:
            raise ValueError(_("The email must be set"))
        email= self.normalize_email(email)
        user= self.model(email=email,**extra_fields)
        
        
        
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,password,**extra_fields):
        """
        Create and save a SuperUser with given email and pass

        Args:
            email (_type_): _description_
            password (_type_): _description_
        """
        
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        extra_fields.setdefault("is_active",True)
        #Extra priv
        extra_fields.setdefault("is_service",True)
        extra_fields.setdefault("is_supplier",True)
        extra_fields.setdefault("is_vendor",True)
        extra_fields.setdefault("is_costumer",True)
        #End here
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("SuperUser must have staff priviledges"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("SuperUser must have superuser priviledges"))
        #extra priv
        if extra_fields.get("is_service") is not True:
            raise ValueError(_("SuperUser must have service priviledges"))
        if extra_fields.get("is_supplier") is not True:
            raise ValueError(_("SuperUser must have supplier priviledges"))
        if extra_fields.get("is_vendor") is not True:
            raise ValueError(_("SuperUser must have vendor priviledges"))
        if extra_fields.get("is_costumer") is not True:
            raise ValueError(_("SuperUser must have costumer priviledges"))
        #end here
        return self.create_user(email,password,**extra_fields)
        # Costumer user 
        
    def create_costumer(self,email,password,**extra_fields):
        """
        Create and save user with costumer form 

        Args:
            email (_type_): _description_
            password (_type_): _description_
        """
        extra_fields.setdefault("is_staff",False)
        extra_fields.setdefault("is_superuser",False)
        extra_fields.setdefault("is_active",True)
        #Extra priv
        extra_fields.setdefault("is_service",False)
        extra_fields.setdefault("is_supplier",False)
        extra_fields.setdefault("is_vendor",False)
        extra_fields.setdefault("is_costumer",True)
        
        if extra_fields.get("is_active") is not True:
            raise ValueError(_("costumer must be active"))
        if extra_fields.get("is_costumer") is not True:
            raise ValueError(_("user must have costumer priviledges"))
        if extra_fields.get("is_staff") is True:
            raise ValueError(_("user is not ment to be staff"))
        if extra_fields.get("is_superuser") is True:
            raise ValueError(_("user is not ment to be superuser"))
        if extra_fields.get("is_service") is True:
            raise ValueError(_("user is not ment to be service"))
        if extra_fields.get("is_supplier") is True:
            raise ValueError(_("user is not ment to be supplier"))
        if extra_fields.get("is_vendor") is True:
            raise ValueError(_("user is not ment to be vendor"))
        
        #end here
        return self.create_user(email,password,**extra_fields)     
    
    #nothing yet
    ''''''