from rest_framework import (
    viewsets,
    status
)
from rest_framework.response import Response
from .models import Thing
from .serializers import ThingSerializer


class ThingViewSet(viewsets.ModelViewSet):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
    filter_fields = ['status', 'kind', 'owner_id']

    def destroy(self, request, pk=None):
        instance = self.get_object()
        if instance.is_owned_by(request.user):
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_403_FORBIDDEN)
