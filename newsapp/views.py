from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
def start(request):
    return render(request, 'newsapp/index.html')
