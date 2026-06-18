from rest_framework import serializers

from customers.models import Kyc


class KycSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kyc
        fields = '__all__'