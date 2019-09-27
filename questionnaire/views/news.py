from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from ..models import News
from ..serializers.news import NewsSerializer

__all__ = ['NewsViewSet']


class NewsViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = News.objects.order_by('-created_at')
    serializer_class = NewsSerializer
