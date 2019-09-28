from django.contrib.admin import ModelAdmin, register, TabularInline
from django_q.admin import QueueAdmin, FailAdmin, TaskAdmin, ScheduleAdmin
from django_q.conf import Conf
from django_q.models import OrmQ, Schedule, Success, Failure

from main.admin import admin_site
from .models.answer import Answer
from .models.answer_variant import AnswerVariant
from .models.comment import Comment
from .models.discussion import Discussion
from .models.like import Like
from .models.news import News
from .models.question import Question
from .models.topic import Topic

admin_site.register(Schedule, ScheduleAdmin)
admin_site.register(Success, TaskAdmin)
admin_site.register(Failure, FailAdmin)

if Conf.ORM or Conf.TESTING:
    admin_site.register(OrmQ, QueueAdmin)


@register(News, site=admin_site)
class NewsAdmin(ModelAdmin):
    list_filter = ('id', 'title', 'created_at')


@register(Comment, site=admin_site)
class CommentAdmin(ModelAdmin):
    list_display = ('id', 'discussion', 'user')


@register(Like, site=admin_site)
class LikeAdmin(ModelAdmin):
    list_display = ('id', 'discussion', 'user', 'value')
    search_fields = ('discussion__name', 'user__full_name')
    list_filter = ('value',)


class DiscussionTable(TabularInline):
    model = Discussion
    classes = ('collapse',)
    fields = ('question', 'answer_type')
    show_change_link = True
    extra = 3


@register(Topic, site=admin_site)
class TopicAdmin(ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class QuestionTable(TabularInline):
    model = Question
    classes = ('collapse',)
    fields = ('question', 'answer_type')
    show_change_link = True
    extra = 3


@register(Discussion, site=admin_site)
class DiscussionAdmin(ModelAdmin):
    list_display = ('id', 'topic', 'name', 'type')
    list_filter = ('type',)
    search_fields = ('topic__name', 'name')
    inlines = (QuestionTable,)


class AnswerVariantTable(TabularInline):
    model = AnswerVariant
    classes = ('collapse',)
    fields = ('variant',)
    extra = 3


@register(Question, site=admin_site)
class QuestionAdmin(ModelAdmin):
    list_display = ('id', 'question', 'answer_type')
    inlines = (AnswerVariantTable,)
    search_fields = ('question',)


@register(Answer, site=admin_site)
class AnswerAdmin(ModelAdmin):
    list_display = ('id', 'question', 'answer')
    list_filter = ('question', 'answer')
    search_fields = ('question__question',)
