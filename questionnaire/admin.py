from django.contrib.admin import ModelAdmin, register, TabularInline

from main.admin import admin_site
from .models.topic import Topic
from .models.discussion import Discussion
from .models.question import Question
from .models.answer import Answer
from .models.answer_variant import AnswerVariant
from .models.comment import Comment
from .models.like import Like
from .models.news import News


@register(News, site=admin_site)
class NewsAdmin(ModelAdmin):
    list_filter = ('id', 'title', 'created_at')


@register(Comment, site=admin_site)
class CommentAdmin(ModelAdmin):
    list_display = ('id', 'discussion', 'user')


@register(AnswerVariant, site=admin_site)
class AnswerVariantAdmin(ModelAdmin):
    list_display = ('id', 'question', 'variant')
    search_fields = ('question__name', 'variant')


@register(Like, site=admin_site)
class LikeAdmin(ModelAdmin):
    list_display = ('id', 'discussion', 'user', 'value')
    search_fields = ('discussion__name', 'user__full_name')
    list_filter = ('value',)


@register(Topic, site=admin_site)
class TopicAdmin(ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@register(Discussion, site=admin_site)
class DiscussionAdmin(ModelAdmin):
    list_display = ('id', 'topic', 'name', 'type')
    list_filter = ('type',)
    search_fields = ('topic__name', 'name')


class AnswerTable(TabularInline):
    model = Answer
    classes = ('collapse',)
    fields = ('id', 'question', 'answer')
    readonly_fields = fields
    extra = 0


@register(Question, site=admin_site)
class QuestionAdmin(ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@register(Answer, site=admin_site)
class AnswerAdmin(ModelAdmin):
    list_display = ('id', 'question', 'answer')
    list_filter = ('question', 'answer')
    search_fields = ('question__name',)
