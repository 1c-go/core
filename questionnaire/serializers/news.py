from rest_framework import serializers

from ..models import News

__all__ = ['NewsSerializer']


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'created_at', 'body')
