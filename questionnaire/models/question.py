from django.db import models

__all__ = ['Question']


class QuestionManager(models.Manager):
    DEFAULT_COUNT = 2

    def _random(self, queryset, count=DEFAULT_COUNT):
        return queryset.order_by('?')[:count]


class Question(models.Model):
    TEXT = 1
    LONG_TEXT = 2
    BOOL = 3
    NUMBER = 4
    SINGLE = 5
    MULTIPLE = 6
    ANSWER_TYPE_CHOICES = (
        (TEXT, 'Текст'),
        (LONG_TEXT, 'Длинный текст'),
        (BOOL, 'Да/Нет'),
        (NUMBER, 'Число'),
        (SINGLE, 'Один вариант ответа'),
        (MULTIPLE, 'Несколько вариантов ответа'),
    )

    discussion = models.ForeignKey(
        verbose_name='Обсуждение', to='questionnaire.Discussion', on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name='Название', max_length=250,
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
        return self.name
