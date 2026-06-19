from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models.role import Role
from ..models.profile import UserProfile
from .profile import UserProfileSerializer

User = get_user_model()


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all())
    profile = UserProfileSerializer(required=False)

    class Meta:
        model = User
        fields = ["email", "username", "password", "role", "profile"]

    def create(self, validated_data):
        profile_data = validated_data.pop("profile", None)
        password = validated_data.pop("password")

        # create user
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        # create profile
        UserProfile.objects.create(
            user=user,
            **(profile_data or {})
        )

        return user