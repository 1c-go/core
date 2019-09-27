from rest_framework import serializers

from ..models import Discussion

__all__ = ['DiscussionSerializer']


class DiscussionSerializer(serializers.ModelSerializer):
    likes = serializers.IntegerField(source='likes_count', read_only=True)
    dislikes = serializers.IntegerField(source='dislikes_count', read_only=True)

    class Meta:
        model = Discussion
        fields = ('id', 'name', 'description', 'likes', 'dislikes')
