from django.db import models

from main.models.user import CustomUser

__all__ = ['Discussion']


class Discussion(models.Model):
    TYPE_CHOICES = CustomUser.TYPE_CHOICES

    topic = models.ForeignKey(
        verbose_name='Тема', to='questionnaire.Topic', on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name='Название', max_length=255,
    )
    description = models.TextField(
        verbose_name='Описание',
    )
    preview = models.CharField(
        verbose_name='Предпросмотр', max_length=100,
    )
    type = models.PositiveSmallIntegerField(
        verbose_name='Тип', choices=TYPE_CHOICES,
    )
    created_at = models.DateTimeField(
        verbose_name='Дата-время создания', auto_now_add=True,
    )
    closed_at = models.DateTimeField(
        verbose_name='Дата-время закрытия', null=True, blank=True,
    )

    class Meta:
        verbose_name = 'Обсуждение'
        verbose_name_plural = 'Обсуждения'
        default_related_name = 'discussions'

    def __str__(self):
        return self.name
