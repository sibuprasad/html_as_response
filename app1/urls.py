app_name='some'

from django.urls import path
from app1.views import *
#from app2.views import *

urlpatterns = [
    path('index/',index,name='index'),
    path('index2/',index2,name='index2'),
]
