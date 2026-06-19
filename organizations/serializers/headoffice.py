from rest_framework import serializers
from organizations.models import HeadOffice


class HeadOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeadOffice
        fields = '__all__'