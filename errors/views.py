import json

from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from .models import Error


# Create your views here.

def get_errors(request, version=1):
    offset = request.GET.get('offset', 0)
    offset = int(offset)
    limit = request.GET.get('limit', 10)
    limit = int(limit)
    search_key = request.GET.get('search_key')
    if search_key:
        error_queryset = Error.objects.filter(error__contains=search_key)
    else:
        error_queryset = Error.objects.all()
    error_queryset = error_queryset[offset:offset + limit]
    error_queryset = error_queryset.values()
    return JsonResponse(list(error_queryset), safe=False)


