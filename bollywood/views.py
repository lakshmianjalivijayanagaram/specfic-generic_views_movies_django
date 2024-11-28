from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def bfi(request):
    return HttpResponse("<h1>bfi's first view</h1>")
def aiswaryarai(request):
    return HttpResponse("<h1><marquee>second generic view---aiswarys is famous bollywood heroine</marquee></h1>")
