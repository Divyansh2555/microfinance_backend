from rest_framework import serializers
from groups.models.groups import Groups

class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = '__all__'