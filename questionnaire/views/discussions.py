from django.db.models import Count, Q
from django_filters import FilterSet, filters
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from ..models import Discussion
from ..serializers.discussion import DiscussionSerializer

__all__ = ['DiscussionsViewSet']


class DiscussionsFilterSet(FilterSet):
    topic = filters.NumberFilter()


class DiscussionsViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Discussion.objects.annotate(likes_count=Count('likes', filter=Q(likes__value=True)),
                                           dislikes_count=Count('likes', filter=Q(likes__value=False))
                                           ).order_by('name')
    serializer_class = DiscussionSerializer
    filterset_class = DiscussionsFilterSet

    def get_queryset(self):
        user = self.request.user
        return super().get_queryset().filter(type=user.type)
