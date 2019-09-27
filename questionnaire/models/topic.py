from django.db import models

__all__ = ['Topic']


class Topic(models.Model):
    name = models.CharField(
        verbose_name='Название', max_length=255,
    )

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.name
