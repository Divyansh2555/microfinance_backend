from rest_framework import serializers
from groups.models import Group_Members

class GroupMembersSerializes(serializers.ModelSerializer):
    class Meta:
        model = Group_Members
        fields = '__all__'