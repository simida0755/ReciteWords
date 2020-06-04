from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic.base import View
from rest_framework import mixins, viewsets
from rest_framework.response import Response

from recitewords.word.models import Word
from recitewords.word.serializers import WordSerializer


class TestView(View):
    def get(self,request):

        word = Word.get_or_spider('foot')
        print(type(word))
        if word:
            import json
            from django.core import serializers
            from django.http import JsonResponse,HttpResponse
            #
            json_data = serializers.serialize('json', word,ensure_ascii=False)
            json_data = json.loads(json_data)
            #In order to allow non-dict objects to be serialized set the safe parameter to False.
            return JsonResponse(json_data,safe=False,json_dumps_params={'ensure_ascii':False})
            # return HttpResponse('hehe')


class WordViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = WordSerializer
    queryset = Word.objects.all()

    def retrieve(self, request, *args, **kwargs):
        # instance = Word.get_or_spider(request['PK'])

        print(kwargs['pk'])
        instance = Word.get_or_spider(kwargs['pk'])
        if not instance:
            return Http404('No %s matches the given word.' % kwargs['pk'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
