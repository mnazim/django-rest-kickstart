from django.contrib import admin
from .models import Thing


class ThingAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'created',
        'modified',
    ]
    search_fields = ['id', 'name']

admin.site.register(Thing, ThingAdmin)
