from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def kfi(request):
    return HttpResponse('<h1>This is specific view of kfi</h1>')
def kgf(request):
    return HttpResponse('<i>this is second specific view-Kollywood</i>')