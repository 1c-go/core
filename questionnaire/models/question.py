from django.db import models

__all__ = ['Question']


class QuestionManager(models.Manager):
    DEFAULT_COUNT = 2

    def _random(self, queryset, count=DEFAULT_COUNT):
        return queryset.order_by('?')[:count]


class Question(models.Model):
    TEXT = 1
    BOOL = 2
    NUMBER = 3
    SINGLE = 4
    MULTIPLE = 5
    ANSWER_TYPE_CHOICES = (
        (TEXT, 'Текст'),
        (BOOL, 'Да/Нет'),
        (NUMBER, 'Число'),
        (SINGLE, 'Один вариант ответа'),
        (MULTIPLE, 'Несколько вариантов ответа'),
    )

    discussion = models.ForeignKey(
        verbose_name='Обсуждение', to='questionnaire.Discussion', on_delete=models.CASCADE,
    )
    question = models.TextField(
        verbose_name='Вопрос',
    )
    answer_type = models.PositiveSmallIntegerField(
        verbose_name='Тип вопроса', choices=ANSWER_TYPE_CHOICES,
    )

    objects = models.Manager()
    random_manager = QuestionManager()

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        default_related_name = 'questions'

    def __str__(self):
        return self.question[:20]
