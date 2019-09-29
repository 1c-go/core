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
    list_display = ('id', 'title', 'created_at')


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
    inlines = (DiscussionTable,)


@register(Comment, site=admin_site)
class CommentAdmin(ModelAdmin):
    list_display = ('id', 'discussion', 'user', 'text', 'sentiment')


@register(Like, site=admin_site)
class LikeAdmin(ModelAdmin):
    list_display = ('id', 'discussion', 'user', 'value')
    search_fields = ('discussion__name', 'user__full_name')
    list_filter = ('value',)


class QuestionTable(TabularInline):
    model = Question
    classes = ('collapse',)
    fields = ('question', 'answer_type')
    show_change_link = True
    extra = 3


class CommentTable(TabularInline):
    model = Comment
    classes = ('collapse',)
    fields = ('user', 'text', 'sentiment')
    readonly_fields = fields
    extra = 0


class LikeTable(TabularInline):
    model = Like
    classes = ('collapse',)
    fields = ('created_at', 'user', 'value')
    readonly_fields = fields
    extra = 0


@register(Discussion, site=admin_site)
class DiscussionAdmin(ModelAdmin):
    list_display = ('id', 'topic', 'name', 'type')
    list_filter = ('type',)
    search_fields = ('topic__name', 'name')
    inlines = (QuestionTable, CommentTable, LikeTable)


class AnswerVariantTable(TabularInline):
    model = AnswerVariant
    classes = ('collapse',)
    fields = ('variant',)
    extra = 3


class AnswerTable(TabularInline):
    model = Answer
    classes = ('collapse',)
    fields = ('user', 'answer', 'sentiment')
    readonly_fields = fields
    extra = 0


@register(Question, site=admin_site)
class QuestionAdmin(ModelAdmin):
    list_display = ('id', 'question', 'answer_type')
    search_fields = ('question',)
    inlines = (AnswerVariantTable, AnswerTable)


@register(Answer, site=admin_site)
class AnswerAdmin(ModelAdmin):
    list_display = ('id', 'question', 'user', 'answer', 'sentiment')
    list_filter = ('question', 'answer')
    search_fields = ('question__question',)
