from django.contrib import admin
from django.urls import path, include

from backend_proj.views import WelcomeView, HealthView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', WelcomeView.as_view()),
    path('health', HealthView.as_view()),
]
