# # users/admin.py
from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User  # Assuming you're using Django's default User model

# from django.contrib import admin
from .models import User

# admin.site.register(User)

# # Customize the UserAdmin class

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'last_login', 'is_active')
    list_filter = ('is_active', 'date_joined')
    search_fields = ('username', 'email', )

# # Register the User model with the customized UserAdmin
# # admin.site.unregister(User)  # Unregister the default UserAdmin
admin.site.register(User, UserAdmin)  # Register the User model with the custom UserAdmin