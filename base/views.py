from __future__ import absolute_import, print_function, unicode_literals
from wolframclient.evaluation import WolframCloudSession
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AudioForm
import numpy as np
import wave
import struct

# Create your views here.
def call(x):
    """ Call the API using function input parameter values.
    If the API was deployed with an export formats set to JSON or WXF, the result is often a native Python type.
    """
    with WolframCloudSession() as session:
        api_response = session.call('https://www.wolframcloud.com/obj/9455e160-850b-499f-97ed-a2fd924e814d', {'x' : x})
        return api_response.get()

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
