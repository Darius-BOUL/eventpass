from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'is_organizer', 'is_staff', 'is_active')
    list_filter = ('is_organizer', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        ('Rôle', {'fields': ('is_organizer',)}),
    )
