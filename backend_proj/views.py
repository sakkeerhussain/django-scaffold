from django.http import JsonResponse
from django.views.generic import View

from backend_proj import config


class WelcomeView(View):

    @staticmethod
    def get(request, *args, **kwargs):
        resp = {
            'status': 'ok',
            'message': 'Welcome to testing backend'
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