from rest_framework import viewsets
from ..models.group_members import Group_Members
from ..serializers.group_members import GroupMembersSerializes


class Group_Members_ViewSet(viewsets.ModelViewSet):
    queryset = Group_Members.objects.all()
    serializer_class = GroupMembersSerializes