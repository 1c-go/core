from django.db import models

__all__ = ['AnswerVariant']


class AnswerVariant(models.Model):
    question = models.ForeignKey(
        verbose_name='Вопрос', to='questionnaire.Question', on_delete=models.PROTECT,
    )
    variant = models.CharField(
        verbose_name='Вариант ответа', max_length=255,
    )

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответов'
        default_related_name = 'answer_variants'

    def __str__(self):
        return f'{self.question} - {self.variant}'
