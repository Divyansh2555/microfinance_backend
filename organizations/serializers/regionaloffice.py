from rest_framework import serializers
from ..models.regional import RegionalOffice


class RegionalOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegionalOffice
        fields = '__all__'