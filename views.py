from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import CustomUser
from django.contrib.auth import authenticate,login,logout
#from .forms import UserCreationForm, LoginForm,FirstUserForm
from .forms import CostumerUserFrom,CostumerUserLogIn,CustomUserChangeForm,CustomUserCreationForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.conf import settings
from django.db import transaction
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.db import models



# Create your views here.

def home(request):
    login_data = CustomUser.objects.all().order_by( 'id').values()
    context= {
    'login_data' : login_data,
    }
    return render(request,'home.html',context=context)


def user_panel(request):
	#mymembers = Member.objects.all().values()
	login_data = CustomUser.objects.all().order_by( 'id').values()
	template = loader.get_template('userpanel.html')
	
	context = { 'login_data': login_data, }
	return HttpResponse(template.render(context,request))
	#return render(request,'all_members.html',context=context)



####SIGN UP PAGE vs1###

def user_signUp(request):
	if request.method == 'POST':
		form= CostumerUserFrom(request.POST)
		
		
  
		if form.is_valid():
			
			
			form.save()
			user=form.cleaned_data.get('email')
			messages.success(request,'Your user was created'+ user)
			return redirect('login')#this line needs to be reviwed
	else:
		form= CostumerUserFrom()
	return render(request, 'signup.html', {'form': form})

####LOG IN PAGE####

####SIGN UP PAGE vs2###




def user_login(request):#this funct need inrovement
	wrong_logs=messages.error(request,"user or passord are wrong")
	if request.method == 'POST':
		form= CostumerUserLogIn(request.POST)
		if form.is_valid():
			email= form.cleaned_data['email']
			password= form.cleaned_data['password']
			user= authenticate(request,email=email,password=password)
			if user:
				login(request, user)

				return redirect('userpanel')
			else:
				wrong_logs
		else:
			print("Error user or pass not provided ny db")

	else:
		form= CostumerUserLogIn()
	return render(request,'login.html',{'form': form})

####LOG OUT PAGE####
def user_logout(request):
	logout(request)
	messages.success(request,"goodbye")
	return redirect('home')
def pass_reset_done(request):
	return request
@csrf_protect
def simulate_csrf_error(request):
	if request.method == 'POST':
		return HttpResponse("Form Submited sucessfully!")
	else:
		return HttpResponse("GET request, please submit the form.")

	
		