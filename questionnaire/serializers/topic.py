from rest_framework import serializers

from ..models import Topic

__all__ = ['TopicSerializer']


class TopicSerializer(serializers.ModelSerializer):
    discussions = serializers.IntegerField(source='discussions__count')

    class Meta:
        model = Topic
        fields = ('id', 'name', 'discussions')
