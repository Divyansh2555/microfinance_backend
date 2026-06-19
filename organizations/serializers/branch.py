from rest_framework import serializers
from ..models.branchoffice import Branch

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'