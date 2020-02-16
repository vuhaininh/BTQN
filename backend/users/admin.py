from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from users import models
from django.contrib.auth.models import Permission


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'first_name', 'last_name']
    fieldsets = (
        (None, {
            'fields': (
                'email',
                'password',
            ),
        }),
        (_('Personal Info'), {
            'fields': ('first_name', 'last_name', 'role')
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser',)
        }),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'role'),
        }),
    )


class RoleAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'permission')


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Role, RoleAdmin)
admin.site.register(Permission)
