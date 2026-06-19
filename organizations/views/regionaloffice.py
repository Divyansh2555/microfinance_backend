from rest_framework import viewsets
from ..models.regional import RegionalOffice
from ..serializers.regionaloffice import  RegionalOfficeSerializer


class RegionOfficeViewSet(viewsets.ModelViewSet):
    queryset = RegionalOffice.objects.all()
    serializer_class = RegionalOfficeSerializer