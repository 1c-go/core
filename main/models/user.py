from django.contrib.auth.models import AbstractUser
from django.db import models

__all__ = ['CustomUser']


class CustomUser(AbstractUser):
    INDIVIDUAL = 0
    ENTITY = 1
    TYPE_CHOICES = (
        (INDIVIDUAL, 'Физ лицо'),
        (ENTITY, 'Юр лицо'),
    )

    first_name = None
    last_name = None
    full_name = models.CharField(
        verbose_name='Имя', max_length=150,
    )
    nickname = models.CharField(
        verbose_name='Ник', max_length=150, unique=True,
    )
    type = models.PositiveSmallIntegerField(
        verbose_name='Тип', choices=TYPE_CHOICES,
    )

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.full_name

    def __str__(self):
        return self.full_name
