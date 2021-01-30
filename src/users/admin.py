from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    models = CustomUser
    add_form = CustomUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            "User Roles",
            {
                "fields":(
                    "is_producer",
                    "is_director",
                )
            }
        )
    )

admin.site.register(CustomUser, CustomUserAdmin)

    

