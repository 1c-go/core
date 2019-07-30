from rest_framework import serializers

from ..models import Question

__all__ = ['QuestionSerializer']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question')
