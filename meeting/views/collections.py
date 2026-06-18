from rest_framework import viewsets
from meeting.models.collection import Collection
from meeting.serializers.collection import CollectionSerializer

class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer