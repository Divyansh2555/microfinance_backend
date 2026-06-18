from rest_framework import viewsets
from ..models.center import Center
from ..serializers.center import CenterSerializer

class CenterViewSet(viewsets.ModelViewSet):
    queryset = Center.objects.all()
    serializer_class = CenterSerializer