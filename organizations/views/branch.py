from rest_framework import viewsets
from ..models.branch import Branch
from ..serializers.branch import BranchSerializer

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer