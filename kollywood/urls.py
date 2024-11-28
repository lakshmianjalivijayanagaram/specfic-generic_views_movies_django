from django.urls import path
from kollywood.views import *
urlpatterns=[
    path('kfi/',kfi,name='kfi'),
    path('kgf/',kgf,name='kgf'),
]