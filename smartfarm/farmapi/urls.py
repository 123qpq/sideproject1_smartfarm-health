from django.urls import path
from .views import check, getfarmdata, appcheck

urlpatterns = [
    path("", getfarmdata.as_view()),
    path("post/", getfarmdata.as_view()),
    path("app/<str:farmid>", appcheck.as_view()),
    path("<str:farmid>/", getfarmdata.as_view()),
    path("<str:farmid>/<str:check>", check.as_view()),
]
