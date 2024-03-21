from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm , CustomUserChangeForm
from .models import CustomUser,Profile,Shop

class CustomUserAdmin(UserAdmin):
    """
    This class add_full list of priviledges for  User Admin Panel

    Args:
        UserAdmin (_type_): _description_
    """
    add_form= CustomUserCreationForm
    form= CustomUserChangeForm
    model= CustomUser
    list_display= ("email","is_staff","is_active","is_service","is_supplier","is_vendor","is_costumer")
    fieldsets= (
        (None,{"fields":("email","password")}),
        ("Permissions", {"fields":("is_staff","is_active","is_service","is_supplier","is_vendor","is_costumer","firstname","lastname",
                                   "groups","user_permissions", )}),
    )

    add_fieldsets= (
        (None,{
            "classes": ("wide",),
            "fields": ("email","password1","password2","is_staff","is_active","is_service","is_supplier","is_vendor","is_costumer","firstname","lastname",
                       "groups","user_permissions")}),
    )
    search_fields= ("email",)
    ordering= ("email",)
    
admin.site.register(CustomUser,CustomUserAdmin)
# Register your models here.
admin.site.register(Profile)
admin.site.register(Shop)