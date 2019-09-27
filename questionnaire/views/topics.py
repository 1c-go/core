from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from ..models import Topic
from ..serializers.topic import TopicSerializer

__all__ = ['TopicsViewSet']


class TopicsViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = Topic.objects.order_by('name')
    serializer_class = TopicSerializer
