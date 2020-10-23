from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from account.models import Account

@admin.register(Account)
class AccountAdmin(BaseUserAdmin):

    list_display = ('email', 'first_name', 'last_name', 'status', 'date_of_birth', 'is_staff',  'is_superuser')
    list_filter = ('status',)
    readonly_fields = ('date_joined','last_login')

    fieldsets = (
        (None, {'fields': ('email', 'is_staff', 'is_superuser', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'status', 'date_of_birth')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'is_staff', 'is_superuser', 'password1', 'password2')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'status', 'date_of_birth')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )

    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ()


# @admin.register(Verification)
# class Verification_Admin(admin.ModelAdmin):

#     list_display = ['user','token','expire_date','create_date']
#     readonly_fields = ['token','expire_date','create_date']