from rest_framework import serializers
from ..models.areaoffice import AreaOffice


class AreaOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaOffice
        fields = '__all__'