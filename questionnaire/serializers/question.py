from rest_framework import serializers

from .answer_variant import AnswerVariantSerializer
from ..models import Question

__all__ = ['QuestionSerializer']


class QuestionSerializer(serializers.ModelSerializer):
    answer_variants = AnswerVariantSerializer(many=True)
    answered = serializers.BooleanField()

    class Meta:
        model = Question
        fields = ('id', 'question', 'answer_type', 'answer_variants', 'answered')
