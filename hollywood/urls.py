from django.urls import path
from hollywood.views import *
urlpatterns=[
    path('hfi/',hfi,name='hfi'),
]