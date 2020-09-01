from django.http import HttpResponse
from django.urls import path

from metromind_backend import config


def index(request):
    print(config.env)
    return HttpResponse("Hello, world. You're at the polls index.")


urlpatterns = [
    path('test/', index),
]
