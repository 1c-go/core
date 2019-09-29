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
    MALE = 1
    FEMALE = 2
    GENDER_CHOICES = (
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
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
    city = models.CharField(
        verbose_name='Город', max_length=50, null=True, blank=True,
    )
    gender = models.PositiveSmallIntegerField(
        verbose_name='Пол', choices=GENDER_CHOICES, null=True, blank=True,
    )
    birthday = models.DateField(
        verbose_name='Дата рождения', null=True, blank=True,
    )

    def get_full_name(self):
        return self.nickname

    def get_short_name(self):
        return self.nickname

    def __str__(self):
        return self.nickname
