from rest_framework import serializers
from customers.models import address
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = address
        fields = '__all__'


