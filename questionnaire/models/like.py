from django.db import models

__all__ = ['Like']


class Like(models.Model):
    discussion = models.ForeignKey(
        verbose_name='Обсуждение', to='questionnaire.Discussion', on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        verbose_name='Пользователь', to='main.CustomUser', on_delete=models.CASCADE,
    )
    value = models.BooleanField(
        verbose_name='Значение',
    )

    class Meta:
        verbose_name = 'Лайк|Дизлайк'
        verbose_name_plural = 'Лайки|Дизлайки'
        unique_together = ('discussion', 'user')
        default_related_name = 'likes'

    def __str__(self):
        return f'{self.discussion} - {self.user} - {self.value}'
