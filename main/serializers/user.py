from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from ..models import CustomUser

__all__ = ['RegistrationSerializer']


class RegistrationSerializer(serializers.ModelSerializer):
    _validator = UniqueValidator(queryset=CustomUser.objects.all())
    email = serializers.EmailField(validators=[_validator], required=False)
    username = serializers.CharField(validators=[_validator])
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ('username', 'full_name', 'email', 'password')

    def get_full_name(self, obj):
        return obj.get_full_name()

    def validate_password(self, value):
        validate_password(value)
        return value
