from django.http import JsonResponse
from django.views.generic import View

from metromind_backend import config


class WelcomeView(View):

    @staticmethod
    def get(request, *args, **kwargs):
        resp = {
            'status': 'ok',
            'message': 'Welcome to MetroMind backend'
        }
        return JsonResponse(resp)


class HealthView(View):

    @staticmethod
    def get(request, *args, **kwargs):
        resp = {
            'status': 'ok',
            'message': 'MetroMind backend is up'
        }
        return JsonResponse(resp)