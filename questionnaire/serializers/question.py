from rest_framework import serializers

from ..models import Question
from .answer_variant import AnswerVariantSerializer

__all__ = ['QuestionSerializer']


class QuestionSerializer(serializers.ModelSerializer):
    answer_variants = AnswerVariantSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', 'name', 'question', 'answer_type', 'answer_variants')
