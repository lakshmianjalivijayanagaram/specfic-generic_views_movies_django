from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def hfi(request):
    return HttpResponse('<h1>This is first specific view of hfi</h1>')