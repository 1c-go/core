from django.db.models import Count, Q, Subquery, OuterRef
from django_filters import FilterSet, filters
from rest_framework import mixins, serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from questionnaire.models.like import Like
from ..models import Discussion
from ..serializers.discussion import DiscussionSerializer

__all__ = ['DiscussionsViewSet']


class CommentParser(serializers.Serializer):
    text = serializers.CharField(allow_blank=False)


class LikeParser(serializers.Serializer):
    value = serializers.BooleanField()


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
        return super().get_queryset().filter(type=user.type).annotate(
            like=Subquery(Like.objects.filter(discussion=OuterRef('id'),
                                              user=user).values('value')[:1]))

    @action(methods=('post',), detail=True)
    def like(self, request, *args, **kwargs):
        context = self.get_serializer_context()
        parser = LikeParser(data=request.data, context=context)
        parser.is_valid(raise_exception=True)

        obj = self.get_object()
        user = request.user

        obj.likes.filter(user=user).delete()
        obj.likes.create(user=user, value=parser.validated_data['value'])
        return Response()

    @action(methods=('post',), detail=True)
    def comment(self, request, *args, **kwargs):
        context = self.get_serializer_context()
        parser = CommentParser(data=request.data, context=context)
        parser.is_valid(raise_exception=True)

        obj = self.get_object()
        user = request.user

        obj.comments.create(user=user, text=parser.validated_data['text'])
        return Response()
