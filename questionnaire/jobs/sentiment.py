import requests

from django.conf import settings

from ..models import Question
from ..models import Answer
from ..models import Comment


url = 'https://russiansentimentanalyzer.p.rapidapi.com/rsa/sentiment/polarity/json/'


def main():
    headers = {'x-rapidapi-key': settings.RAPIDAPI_KEY}
    qs = Answer.objects.filter(sentiment=None, question__answer_type__in=(Question.TEXT,
                                                                          Question.LONG_TEXT)
                               ).values(article_id='id', text='answer')[:50]
    data = list(qs)
    response = requests.post(url, headers=headers, json=data)
    if response.ok:
        response_data = response.json()
        answer = qs.get(id=response_data['article_id'])
        answer.sentiment = response_data['strength']
        answer.save()

    qs = Comment.objects.filter(sentiment=None).values(article_id='id', text='answer')[:50]
    data = list(qs)
    response = requests.post(url, headers=headers, json=data)
    if response.ok:
        response_data = response.json()
        comment = qs.get(id=response_data['article_id'])
        comment.sentiment = response_data['strength']
        comment.save()
