from django.views.generic.base import View
from rest_framework import mixins, viewsets

from recitewords.word.models import Word
from recitewords.word.serializers import WordSerializer


class Word_bookView(viewsets.ModelViewSet):

    pass
