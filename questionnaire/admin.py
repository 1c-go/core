from django.contrib.admin import ModelAdmin, register, TabularInline

from main.admin import admin_site
from .models.question import Question
from .models.answer import Answer


class AnswerTable(TabularInline):
    model = Answer
    classes = ('collapse',)
    fields = ('id', 'question', 'answer')
    readonly_fields = fields
    extra = 0


@register(Question, site=admin_site)
class QuestionAdmin(ModelAdmin):
    list_display = ('id', 'name', 'positive_answer')
    list_filter = ('positive_answer',)
    search_fields = ('name',)


@register(Answer, site=admin_site)
class AnswerAdmin(ModelAdmin):
    list_display = ('id', 'question', 'answer')
    list_filter = ('question', 'answer')
    search_fields = ('question__name',)
