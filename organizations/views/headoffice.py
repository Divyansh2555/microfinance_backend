from rest_framework import viewsets
from ..models.headoffice import HeadOffice
from ..serializers.headoffice import HeadOfficeSerializer

class HeadOfficeViewSet(viewsets.ModelViewSet):
    queryset = HeadOffice.objects.all()
    serializer_class = HeadOfficeSerializer