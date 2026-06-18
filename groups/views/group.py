from rest_framework import viewsets
from ..serializers.group import GroupsSerializer
from ..models.groups import Groups

class Group_viewSet(viewsets.ModelViewSet):
    queryset = Groups.objects.all()
    serializer_class = GroupsSerializer