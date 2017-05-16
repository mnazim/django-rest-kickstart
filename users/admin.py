from django.contrib import admin
from django.utils.translation import ugettext as _
from custom_user.admin import EmailUserAdmin
from django.contrib.postgres.fields import JSONField

from .models import User


class UserAdmin(EmailUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('JSON Depot'), {'fields': ('depot',)}),
    )
    list_display = [
        'id',
        'email',
        'is_active',
        'is_staff',
        'is_superuser',
    ]
    list_filter = ['is_active', 'is_staff', 'is_superuser']
    search_fields = ['id', 'email']


admin.site.register(User, UserAdmin)
