# Generated by Django 2.2.5 on 2019-09-27 20:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0010_news'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='like',
            options={'default_related_name': 'likes', 'verbose_name': 'Лайк | Дизлайк', 'verbose_name_plural': 'Лайки | Дизлайки'},
        ),
        migrations.AddField(
            model_name='answer',
            name='sentiment',
            field=models.FloatField(blank=True, null=True, verbose_name='Настроение'),
        ),
        migrations.AddField(
            model_name='comment',
            name='sentiment',
            field=models.FloatField(blank=True, null=True, verbose_name='Настроение'),
        ),
        migrations.AddField(
            model_name='like',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Создан'),
            preserve_default=False,
        ),
    ]
