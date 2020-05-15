from django.views.generic.base import View
from rest_framework import mixins, viewsets

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
