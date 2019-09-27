from rest_framework import routers

from questionnaire.views.comments import CommentsViewSet
from .views.discussions import DiscussionsViewSet
from .views.questions import QuestionsViewSet
from .views.topics import TopicsViewSet

router = routers.DefaultRouter()
router.register('topics', TopicsViewSet)
router.register('discussions', DiscussionsViewSet)
router.register('questions', QuestionsViewSet)
router.register('comments', CommentsViewSet)
