from django.contrib import admin
from apps.users_app.models import User
from apps.auth_app.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import admin as auth_admin

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('email',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'is_staff')
    search_fields = ('username', 'email')
    ordering = ('username',)

# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     search_fields = ('id', 'first_name', 'last_name')
#     list_display = ( "user", "first_name", "last_name", "balance",'role')
#     list_editable = ('role', 'balance')
