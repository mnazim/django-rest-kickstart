from rest_framework import viewsets
from .models import Thing
from .serializers import ThingSerializer


class ThingViewSet(viewsets.ModelViewSet):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
