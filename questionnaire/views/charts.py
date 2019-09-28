from django.db.models import Count, IntegerField, F
from django.db.models.functions import Cast, Now
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import CustomUser
from ..models import Answer
from ..models import Discussion


class ChartDataLikes(APIView):
    def get(self, request, *args, **kwargs):
        dis = Discussion.objects.get(pk=request.query_params.get('discussion'))
        likes = dis.likes.filter(value=True).count()
        dislikes = dis.likes.filter(value=False).count()
        return Response({
            'labels': ['лайки', 'дизлайки'],
            'datasets': [{
                'data': [likes, dislikes],
                'backgroundColor': [
                    'rgba(54, 162, 235, 0.4)',
                    'rgba(255, 99, 132, 0.4)',
                ],
            }]
        })


class ChartDataGender(APIView):
    def get(self, request, *args, **kwargs):
        dis = Discussion.objects.get(pk=request.query_params.get('discussion'))
        male = Answer.objects.filter(question__discussion=dis, user__gender=CustomUser.MALE).distinct().count()
        female = Answer.objects.filter(question__discussion=dis, user__gender=CustomUser.FEMALE).distinct().count()
        return Response({
            'labels': ['Мужчины', 'Женщины'],
            'datasets': [{
                'data': [male, female],
                'backgroundColor': [
                    'rgba(54, 162, 235, 0.4)',
                    'rgba(255, 99, 132, 0.4)',
                ],
            }]
        })


class ChartDataCity(APIView):
    def get(self, request, *args, **kwargs):
        dis = Discussion.objects.get(pk=request.query_params.get('discussion'))
        users = CustomUser.objects.filter(answers__question__discussion=dis).order_by('city')
        data = list(users.annotate(Count('city')).values('city', 'city__count'))
        return Response({
            'labels': [city['city'] for city in data],
            'datasets': [{
                'data': [city['city__count'] for city in data],
                'backgroundColor': [
                    'rgba(54, 162, 235, 0.4)',
                    'rgba(255, 99, 132, 0.4)',
                ],
                'label': 'Города'
            }]
        })


class ChartDataAge(APIView):
    def get(self, request, *args, **kwargs):
        dis = Discussion.objects.get(pk=request.query_params.get('discussion'))
        users = CustomUser.objects.filter(answers__question__discussion=dis).annotate(
            age=Cast(Now() - F('birthday'), output_field=IntegerField()))
        data = list(users.values('age').annotate(Count('age')).values('age', 'age__count'))
        return Response({
            'labels': [age['age'] for age in data],
            'datasets': [{
                'data': [age['age__count'] for age in data],
                'backgroundColor': [
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 99, 132, 0.2)',
                ],
                'label': 'Возраст'
            }]
        })


line_chart = TemplateView.as_view(template_name='questionnaire/chart.html')
