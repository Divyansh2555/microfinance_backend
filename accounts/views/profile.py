from rest_framework import viewsets
from ..models.profile import UserProfile
from ..serializers.profile import UserProfileSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


