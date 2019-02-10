from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'release/index.html', {})

def about(request):
    return render(request, 'release/about.html', {})

def recruiting(request):
    return render(request, 'release/recruiting.html', {})
