from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from ..models import CustomUser

__all__ = ['RegistrationSerializer', 'ViewNicknameSerializer', 'ProfileSerializer',
           'ProfileEditSerializer']


class RegistrationSerializer(serializers.ModelSerializer):
    _validator = UniqueValidator(queryset=CustomUser.objects.all())
    email = serializers.EmailField(validators=[_validator], required=False)
    username = serializers.CharField(validators=[_validator])
    nickname = serializers.CharField(validators=[_validator])

    class Meta:
        model = CustomUser
        fields = ('username', 'nickname', 'full_name', 'email', 'password', 'type', 'city',
                  'gender', 'birthday')

    def validate_password(self, value):
        validate_password(value)
        password = make_password(value)
        return password


class ViewNicknameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'nickname')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'full_name', 'nickname', 'email', 'username', 'type', 'city', 'gender',
                  'birthday')


class ProfileEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'full_name', 'email', 'city', 'gender', 'birthday')
