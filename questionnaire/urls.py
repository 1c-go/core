from django.urls import re_path, include
from rest_framework import routers

from questionnaire.views.comments import CommentsViewSet
from questionnaire.views.news import NewsViewSet
from .views.discussions import DiscussionsViewSet
from .views.questions import QuestionsViewSet
from .views.topics import TopicsViewSet

router = routers.DefaultRouter()
router.register('topics', TopicsViewSet)
router.register('discussions', DiscussionsViewSet)
router.register('questions', QuestionsViewSet)
router.register('comments', CommentsViewSet)
router.register('news', NewsViewSet)

urlpatterns = [
    re_path('', include(router.urls)),
]
