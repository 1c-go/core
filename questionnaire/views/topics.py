from django.db.models import Count
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from ..models import Topic
from ..serializers.topic import TopicSerializer

__all__ = ['TopicsViewSet']


class TopicsViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = Topic.objects.annotate(Count('discussions')).filter(
        discussions__count__gte=0).order_by('name')
    serializer_class = TopicSerializer
