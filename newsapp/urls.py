from tracemalloc import start
from django.urls import URLPattern, path
from .views import *

urlpatterns = [
    path('', start, name="base"),
]