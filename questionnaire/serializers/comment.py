from rest_framework import serializers

from main.serializers.user import ViewNicknameSerializer
from ..models import Comment

__all__ = ['CommentSerializer']


class CommentSerializer(serializers.ModelSerializer):
    user = ViewNicknameSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'user', 'text')
