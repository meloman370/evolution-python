from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from api.serializers.user_profile import UserProfileSerializer

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        Return profile by authenticated user
        """
        user = request.user
        serializer = UserProfileSerializer(user.userprofile)
        return Response(serializer.data, status=status.HTTP_200_OK)
