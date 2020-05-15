from django.urls import path

from recitewords.test.views import *

app_name = "test"
urlpatterns = [
     path("<word>", view=WordView.as_view(), name="word"),
]
