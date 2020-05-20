from django.urls import path

from recitewords.word.views import *

app_name = "word"
urlpatterns = [
    path("<str:name>", view=WordViewSet.as_view({'get',}), name="test"),
]
