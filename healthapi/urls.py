from django.urls import path
from .views import gethealthdata

urlpatterns = [
    path("", gethealthdata.as_view()),
    path("post/", gethealthdata.as_view()),
    path("<str:username>/", gethealthdata.as_view()),
]
