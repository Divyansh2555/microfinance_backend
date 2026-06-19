from rest_framework import viewsets
from organizations.models import AreaOffice
from ..serializers.areaoffice import AreaOfficeSerializer

class AreaOfficeViewSet(viewsets.ModelViewSet):
    queryset = AreaOffice.objects.all()
    serializer_class = AreaOfficeSerializer