from django.contrib import admin
from .models import User
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'last_login', 'is_active')
    list_filter = ('is_active', 'date_joined')
    search_fields = ('username', 'email', )

admin.site.register(User, UserAdmin)  