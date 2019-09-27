from django.db import models

__all__ = ['Answer']


class Answer(models.Model):
    question = models.ForeignKey(
        verbose_name='Вопрос', to='questionnaire.Question', on_delete=models.PROTECT,
    )
    answer = models.CharField(
        verbose_name='Ответ', null=True, blank=True, max_length=255,
    )
    user = models.ForeignKey(
        verbose_name='Пользователь', to='main.CustomUser', on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Ответ на вопрос'
        verbose_name_plural = 'Ответы на вопросы'
        unique_together = ('question', 'user')
        default_related_name = 'answers'

    def __str__(self):
        return f'{self.question} - {self.answer}'
