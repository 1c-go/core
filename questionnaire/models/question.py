from django.db import models

__all__ = ['Question']


class QuestionManager(models.Manager):
    DEFAULT_COUNT = 2

    def _random(self, queryset, count=DEFAULT_COUNT):
        return queryset.order_by('?')[:count]


class Question(models.Model):
    name = models.CharField(
        verbose_name='Название', max_length=250,
    )
    question = models.TextField(
        verbose_name='Вопрос',
    )
    positive_answer = models.BooleanField(
        verbose_name='Положительный ответ',
    )

    objects = models.Manager()
    random_manager = QuestionManager()

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.name
