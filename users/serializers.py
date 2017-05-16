from helpers.serializers import BaseModelSerializer
from .models import User

class UserSerializer(BaseModelSerializer):
    class Meta:
        model = User
        fields = [
            'pk',
            'email',
            'is_active',
            'is_staff',
            'is_superuser',
        ]
