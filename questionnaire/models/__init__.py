from django.db.models import Count, FloatField, F, Q
from django.db.models.functions import Cast

from .question import *
from .answer import *

__all__ = ['calc_rate']
__all__ += question.__all__
__all__ += answer.__all__


def calc_rate(queryset, rate_scale=5):
    queryset = (queryset.annotate(
        answers=Count('record__answer', filter=Q(record__answer__answer__isnull=False)),
        positive_answers=Count('record__answer', filter=Q(
            record__answer__answer=F('record__answer__question__positive_answer')) & Q(
            record__answer__answer__isnull=False))
    ).annotate(
        answers=Cast('answers', FloatField()),
        positive_answers=Cast('positive_answers', FloatField())
    ).annotate(rate=F('positive_answers') / F('answers') * rate_scale)
     .order_by('-rate'))
    return queryset
