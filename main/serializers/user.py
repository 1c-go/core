from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from ..models import CustomUser

__all__ = ['RegistrationSerializer', 'ViewNicknameSerializer']


class RegistrationSerializer(serializers.ModelSerializer):
    _validator = UniqueValidator(queryset=CustomUser.objects.all())
    email = serializers.EmailField(validators=[_validator], required=False)
    username = serializers.CharField(validators=[_validator])
    nickname = serializers.CharField(validators=[_validator])

    class Meta:
        model = CustomUser
        fields = ('username', 'nickname', 'full_name', 'email', 'password', 'type')

    def validate_password(self, value):
        validate_password(value)
        return value


class ViewNicknameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'nickname')
