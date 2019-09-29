from uuid import uuid4

from django.conf import settings
from django.core.mail import send_mail
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from ..serializers.token import CustomTokenObtainSerializer
from ..serializers.user import RegistrationSerializer

__all__ = ['CustomTokenObtainView', 'RegistrationView']


class CustomTokenObtainView(TokenObtainPairView):
    serializer_class = CustomTokenObtainSerializer


class RegistrationView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        if serializer.email:
            code = uuid4()
            send_mail('Подтверждение почты', f'https://jlemyp.ru:8000/verify-email/{code}/',
                      settings.DEFAULT_FROM_EMAIL, [serializer.email])
        return Response()
