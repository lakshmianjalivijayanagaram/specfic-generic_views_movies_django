from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def tfi(request):
    return HttpResponse('<h1>This is tfi first view</h1>')
def rrr(request):
    return HttpResponse('<h1><marquee>This is tollywood second generic view -RRR</marquee></h1>')
