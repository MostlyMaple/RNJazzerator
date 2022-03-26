from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AudioForm
import numpy as np
import wave
import struct

# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html', context)

def genPrimes(request):
    form = AudioForm()
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context = {'form': form}
            return render(request, 'gen-primes.html', context)
    context = {'form': form}
    return render(request, 'gen-primes.html', context)

def piano(request):
    context = {}
    return render(request, 'piano.html', context)
