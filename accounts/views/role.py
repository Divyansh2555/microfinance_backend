from rest_framework import viewsets
from accounts.models import Role
from accounts.serializers import RoleSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer