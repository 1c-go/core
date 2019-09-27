# Generated by Django 2.2.5 on 2019-09-27 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questionnaire', '0004_auto_20190927_1914'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answervariant',
            options={'default_related_name': 'answer_variants', 'verbose_name': 'Вариант ответа', 'verbose_name_plural': 'Варианты ответов'},
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together={('question', 'user')},
        ),
    ]
