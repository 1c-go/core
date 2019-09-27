from rest_framework import serializers

from ..models import AnswerVariant

__all__ = ['AnswerVariantSerializer']


class AnswerVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerVariant
        fields = ('id', 'variant')
