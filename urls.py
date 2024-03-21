from django.urls import path
from . import views
from .manager import abusers
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('abusers/login/',views.user_login, name='login'),
    path('abusers/logout/',views.user_logout, name='logout'),
    path('abusers/signup/',views.user_signUp, name='signup'),
    path('userpanel/',views.user_panel,name='userpanel'),
    
    

	      ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)