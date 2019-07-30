from django.db import models

__all__ = ['Answer']


class Answer(models.Model):
    question = models.ForeignKey(
        verbose_name='Вопрос', to='questionnaire.Question', on_delete=models.PROTECT,
    )
    answer = models.BooleanField(
        verbose_name='Ответ', null=True, blank=True,
    )

    class Meta:
        verbose_name = 'Ответ на вопрос'
        verbose_name_plural = 'Ответы на вопросы'

    def __str__(self):
        return f'{self.question} - {self.answer}'
