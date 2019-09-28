from django.urls import path, re_path, include
from rest_framework import routers

from .views.comments import CommentsViewSet
from .views.news import NewsViewSet
from .views.discussions import DiscussionsViewSet
from .views.questions import QuestionsViewSet
from .views.topics import TopicsViewSet
from .views.charts import line_chart, ChartDataLikes, ChartDataGender, ChartDataCity, ChartDataAge

router = routers.DefaultRouter()
router.register('topics', TopicsViewSet)
router.register('discussions', DiscussionsViewSet)
router.register('questions', QuestionsViewSet)
router.register('comments', CommentsViewSet)
router.register('news', NewsViewSet)

urlpatterns = [
    re_path('', include(router.urls)),
    path('chart', line_chart),
    path('chart-likes', ChartDataLikes.as_view(), name='chart-likes'),
    path('chart-gender', ChartDataGender.as_view(), name='chart-gender'),
    path('chart-city', ChartDataCity.as_view(), name='chart-city'),
    path('chart-age', ChartDataAge.as_view(), name='chart-age'),
]
