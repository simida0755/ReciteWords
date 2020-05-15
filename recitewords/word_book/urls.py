from django.urls import path

from recitewords.word.views import *

app_name = "word"
urlpatterns = [
    path("test/", view=TestView.as_view(), name="test"),
]
