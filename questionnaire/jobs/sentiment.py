import requests
from django.conf import settings
from django.db.models import F

from ..models import Answer
from ..models import Comment
from ..models import Question

url = 'https://russiansentimentanalyzer.p.rapidapi.com/rsa/sentiment/polarity/jsons/'


def sentiment_objects(qs, manager, headers):
    data = list(qs)
    if not data:
        return
    response = requests.post(url, headers=headers, json=data)
    if not response.ok:
        return

    response_data = response.json()
    for sentiment in response_data:
        obj = manager.get(id=sentiment['article_id'])
        obj.sentiment = sentiment['strength']
        obj.save()


def main():
    headers = {'x-rapidapi-key': settings.RAPIDAPI_KEY}
    qs = Answer.objects.filter(sentiment=None, question__answer_type=Question.TEXT).values(
        article_id=F('id'), text=F('answer'))[:50]
    sentiment_objects(qs, Answer.objects, headers)

    qs = Comment.objects.filter(sentiment=None).values().values(article_id=F('id'),
                                                                text=F('text'))[:50]
    sentiment_objects(qs, Comment.objects, headers)
