from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers.user import ProfileSerializer, ProfileEditSerializer

__all__ = ['ProfileViewSet']


class ProfileViewSet(APIView):
    def get(self, request, *args, **kwargs):
        data = ProfileSerializer(request.user).data
        return Response(data)

    def post(self, request, *args, **kwargs):
        serializer = ProfileEditSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response()
