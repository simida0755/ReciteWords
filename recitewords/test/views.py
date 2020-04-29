from django.views.generic.base import View

from recitewords.spider.html_word_spider import SpiderWord


class WordView(View):
    def get(self):
        word = self.kwargs['word']
        spider = SpiderWord('lj:good')

        import json
        from django.core import serializers
        from django.http import JsonResponse
        #
        # json_data = serializers.serialize('json',spider.centences,ensure_ascii=False)
        json_data = json.dumps(spider.centences, ensure_ascii=False)
        #In order to allow non-dict objects to be serialized set the safe parameter to False.
        return JsonResponse(json_data,safe=False,json_dumps_params={'ensure_ascii':False})
