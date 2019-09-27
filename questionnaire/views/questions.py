from django_filters import FilterSet, filters
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from ..models import Question
from ..serializers.question import QuestionSerializer

__all__ = ['QuestionsViewSet']


class QuestionsFilterSet(FilterSet):
    discussion = filters.NumberFilter()


class QuestionsViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filterset_class = QuestionsFilterSet
