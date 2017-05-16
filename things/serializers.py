from helpers.serializers import BaseModelSerializer
from .models import Thing

class ThingSerializer(BaseModelSerializer):
    class Meta:
        model = Thing
        fields = [
            'pk',
            'name',
        ]
