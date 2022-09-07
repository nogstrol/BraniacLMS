from django.shortcuts import render
import sys


def hello_world(request):
    return HttpResponse("Hello!")