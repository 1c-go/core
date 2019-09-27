from django_filters import FilterSet, filters
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from ..models import Comment
from ..serializers.comment import CommentSerializer

__all__ = ['CommentsViewSet']


class CommentsFilterSet(FilterSet):
    discussion = filters.NumberFilter()


class CommentsViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filterset_class = CommentsFilterSet
