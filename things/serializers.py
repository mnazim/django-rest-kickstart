from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)
from rest_framework import serializers
from helpers.serializers import BaseModelSerializer
from .models import Thing

class ThingSerializer(TaggitSerializer, BaseModelSerializer):
    tags = TagListSerializerField()
    owner_id = serializers.SerializerMethodField()
    class Meta:
        model = Thing
        fields = [
            'id',
            'name',
            'owner_id',
            'status',
            'kind',
            'tags',
        ]

    def get_owner_id(self, instance):
        return str(instance.owner_id)
