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
    type = models.PositiveSmallIntegerField(
        verbose_name='Тип', choices=TYPE_CHOICES,
    )

    class Meta:
        verbose_name = 'Обсуждение'
        verbose_name_plural = 'Обсуждения'
        default_related_name = 'discussions'

    def __str__(self):
        return self.name
