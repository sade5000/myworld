from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from .models import CustomUser
from django import forms
from django.forms import Form


from django.core.validators import validate_email
from django.contrib.auth.password_validation import validate_password

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields= ("email","password1","password2","is_costumer")
        """
        It show just email field for now 
        
        Args:
            model (_type_): _description_
            fields (_type_): _description_
        
        """
    
      

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields= ("email",)
###create service form
class CostumerUserFrom(UserCreationForm):
    class Meta:
        model = CustomUser
        fields= ("email","password1","password2","is_costumer")
    is_costumer= forms.BooleanField()
        
class CostumerUserLogIn(forms.Form):
    """
    This should be a test form for Costumes Users Form

    Args:
        CustomUserCreationForm (_type_): _description_
    
    """
    
    email=forms.EmailField(validators=[validate_email],widget=forms.EmailInput())
    password=forms.CharField(max_length=40,widget=forms.PasswordInput())
    

	

		