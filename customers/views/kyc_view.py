from rest_framework import viewsets
from  ..models.kyc import Kyc
from ..serializers.kyc_serializer import KycSerializer


class KycViewSet(viewsets.ModelViewSet):
    queryset = Kyc.objects.all()
    serializer_class = KycSerializer