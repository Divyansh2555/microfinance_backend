from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.signup import SignupSerializer


class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            return Response({
                "message": "User created successfully",
                "user_id": user.id,
                "email": user.email,
                "role": user.role.name if user.role else None
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)