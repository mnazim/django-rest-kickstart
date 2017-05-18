from django.contrib import admin
from .models import Thing


class ThingAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'kind',
        'owner',
        'tag_list',
        'status',
        'created',
        'modified',
    ]
    search_fields = ['id', 'name']
    list_filter = [
        'kind',
        'status',
    ]

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


admin.site.register(Thing, ThingAdmin)
