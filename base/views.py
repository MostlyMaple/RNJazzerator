from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html', context)

def genPrimes(request):
    context = {}
    return render(request, 'gen-primes.html', context)

def piano(request):
    context = {}
    return render(request, 'piano.html', context)
