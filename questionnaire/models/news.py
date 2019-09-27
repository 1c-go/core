from django.db import models

__all__ = ['News']


class News(models.Model):
    created_at = models.DateTimeField(
        verbose_name='Дата-время создания', auto_now_add=True,
    )
    title = models.CharField(
        verbose_name='Заголовок', max_length=255,
    )
    body = models.TextField(
        verbose_name='Тело',
    )

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.name
