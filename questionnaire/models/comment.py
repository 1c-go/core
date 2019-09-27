from django.db import models

__all__ = ['Comment']


class Comment(models.Model):
    discussion = models.ForeignKey(
        verbose_name='Обсуждение', to='questionnaire.Discussion', on_delete=models.PROTECT,
    )
    user = models.ForeignKey(
        verbose_name='Пользователь', to='main.CustomUser', on_delete=models.CASCADE,
    )
    text = models.TextField(
        verbose_name='Текст',
    )
    sentiment = models.FloatField(
        verbose_name='Настроение', null=True, blank=True,
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        default_related_name = 'comments'

    def __str__(self):
        return f'{self.discussion} - {self.user} - {self.text[:10]}'
