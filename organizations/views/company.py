from rest_framework import serializers, viewsets
from ..models.company import Company
from ..serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer