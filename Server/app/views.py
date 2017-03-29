from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from rest_framework.parsers import JSONParser

from django.views.decorators.csrf import csrf_exempt

from .models import User


@csrf_exempt
def login(request):
    pass
