from django_filters import FilterSet, filters
from rest_framework import mixins, serializers
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ..models import Question
from ..serializers.question import QuestionSerializer

__all__ = ['QuestionsViewSet']


class AnswerParser(serializers.Serializer):
    answer = serializers.CharField(min_length=1)

    def validate(self, attrs):
        def boolean(value):
            if value not in ('true', 'false'):
                raise ValueError()

        def single(value):
            if not question.answer_variants.filter(id=int(value)).exists():
                raise ValueError()

        def multiple(value):
            values = list(map(int, value.split(',')))
            count = question.answer_variants.filter(id__in=values).count()
            if len(values) != count:
                raise ValueError()

        question = self.context['view'].get_object()
        validators = {
            Question.TEXT: lambda x: x,
            Question.LONG_TEXT: lambda x: x,
            Question.BOOL: boolean,
            Question.NUMBER: lambda x: float(x.replace(',' '.')),
            Question.SINGLE: single,
            Question.MULTIPLE: multiple,
        }
        try:
            validators[question.answer_type](attrs['answer'])
        except ValueError:
            raise ValidationError('Неверный формат ответа')
        return attrs


class QuestionsFilterSet(FilterSet):
    discussion = filters.NumberFilter()


class QuestionsViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filterset_class = QuestionsFilterSet

    @action(methods=('post',), detail=True)
    def answer(self, request, *args, **kwargs):
        context = self.get_serializer_context()
        parser = AnswerParser(data=request.data, context=context)
        parser.is_valid(raise_exception=True)

        obj = self.get_object()
        user = request.user

        obj.answers.filter(user=user).delete()
        obj.answers.create(user=user, answer=parser.validated_data['answer'])
        return Response()
