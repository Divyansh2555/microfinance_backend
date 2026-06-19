from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login
from ..serializers.login import LoginSerializer


class LoginView(APIView):
    authentication_classes = []  # login ke liye auth required nahi hota
    permission_classes = []

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]

        # session login (optional but real Django usage)
        login(request, user)

        return Response(
            {
                "success": True,
                "message": "Login successful",
                "data": {
                    "user_id": user.id,
                    "email": user.email,
                    "username": user.username,
                    "role": user.role.name if user.role else None,
                },
            },
            status=status.HTTP_200_OK
        )