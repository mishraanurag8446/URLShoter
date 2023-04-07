from django.urls import path
from .views import get_short_url, shorten_url

urlpatterns = [
    path('short/', shorten_url, name='short-url'),
    path('<str:short_code>', get_short_url, name='get-short-url')
]
