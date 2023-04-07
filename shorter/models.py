from django.db import models
from django.http import HttpResponse
from django.shortcuts import redirect


class URL(models.Model):
    original_url = models.URLField(max_length=500)
    short_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)


