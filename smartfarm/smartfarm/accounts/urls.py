from django.urls import path, include
from .views import signin, signup

urlpatterns = [
    path("signup/", signup.as_view()),
    path("signin/", signin.as_view()),
]
