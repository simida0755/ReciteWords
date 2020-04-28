from django.urls import path

from recitewords.test.views import *

app_name = "test"
urlpatterns = [
    path("test/", view=TestView.as_view(), name="test"),
]
