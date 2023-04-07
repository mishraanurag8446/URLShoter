from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import redirect
from django.http import HttpResponse
from django.utils.crypto import get_random_string
from .models import URL


@api_view(['POST'])
def shorten_url(request):
    if request.method == 'POST':
        original_url = request.data.get('original_url')
        short_code = get_random_string(length=6)
        url = URL(original_url=original_url, short_code=short_code)
        url.save()
        return Response({'short_url': request.build_absolute_uri('/') + short_code})
    return Response()


@api_view(['GET'])
def get_short_url(request, short_code):
    try:
        url = URL.objects.get(short_code=short_code)
        return redirect(url.original_url)
    except URL.DoesNotExist:
        return HttpResponse('Short URL not found')
