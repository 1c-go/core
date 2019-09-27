import requests

from django.conf import settings
from django.db.models import F

from ..models import Question
from ..models import Answer
from ..models import Comment


url = 'https://russiansentimentanalyzer.p.rapidapi.com/rsa/sentiment/polarity/jsons/'


def main():
    headers = {'x-rapidapi-key': settings.RAPIDAPI_KEY}
    qs = Answer.objects.filter(sentiment=None, question__answer_type__in=(Question.TEXT,
                                                                          Question.LONG_TEXT)
                               ).values(article_id=F('id'), text=F('answer'))[:50]
    data = list(qs)
    print(data)
    if data:
        response = requests.post(url, headers=headers, json=data)
        if response.ok:
            response_data = response.json()
            for sentiment in response_data:
                answer = Answer.objects.get(id=sentiment['article_id'])
                answer.sentiment = sentiment['strength']
                answer.save()
                print(answer, answer.sentiment)

    qs = Comment.objects.filter(sentiment=None).values().values(article_id=F('id'), text=F('text'))[:50]
    data = list(qs)
    print(data)
    if data:
        response = requests.post(url, headers=headers, json=data)
        if response.ok:
            response_data = response.json()
            for sentiment in response_data:
                comment = Comment.objects.get(id=sentiment['article_id'])
                comment.sentiment = sentiment['strength']
                comment.save()
                print(comment, comment.sentiment)
