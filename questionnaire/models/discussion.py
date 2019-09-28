import requests
from django.db import models

from main.models.user import CustomUser

__all__ = ['Discussion']


class Discussion(models.Model):
    TYPE_CHOICES = CustomUser.TYPE_CHOICES

    topic = models.ForeignKey(
        verbose_name='Тема', to='questionnaire.Topic', on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name='Название', max_length=255,
    )
    description = models.TextField(
        verbose_name='Описание',
    )
    preview = models.CharField(
        verbose_name='Предпросмотр', max_length=100,
    )
    type = models.PositiveSmallIntegerField(
        verbose_name='Тип', choices=TYPE_CHOICES,
    )
    created_at = models.DateTimeField(
        verbose_name='Дата-время создания', auto_now_add=True,
    )
    closed_at = models.DateTimeField(
        verbose_name='Дата-время закрытия', null=True, blank=True,
    )

    class Meta:
        verbose_name = 'Обсуждение'
        verbose_name_plural = 'Обсуждения'
        default_related_name = 'discussions'

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        new = not self.id
        super().save(force_insert, force_update, using, update_fields)

        if new:
            data = {
                'notification': {
                    'body': self.preview,
                    'title': 'Новое обсуждение',
                    'sound': 'default'
                },
                'priority': 'high',
                'data': {
                    'click_action': 'FLUTTER_NOTIFICATION_CLICK',
                    'id': '1',
                    'status': 'done'
                },
                'to': 'cJB0a_cN1Us:APA91bFuZ47cosiH3NafguF7GdHySh_lbR5_B2LCs29Fh7tCVZSeip46LMiYuBiQGZo'
                      'Dbx9fss4SwOwZxjh2tVcDtGZTnhlyBdzaqRRFfC4oEiowhe0_bhZfCyInPw_SRxKf_cX-T2G6'
            }
            response = requests.post('https://fcm.googleapis.com/fcm/send', json=data, headers={
                'Authorization': 'key=AAAA5AXWsQU:APA91bH9WJLN4IDMMBb631TzHuQCPrmTMZyZ328mIEPWgedff'
                                 'YZTjxRL5_WQ6g_vT5lbbHNBZDiCQCgG6ydAkH2fpsZW5zGp_IYKTNu5YUSOAngT'
                                 'zoviK66LNGCATR1p3EeOcBac5E2n'
            })
            print(response.content)
