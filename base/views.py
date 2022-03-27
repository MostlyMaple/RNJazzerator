from __future__ import absolute_import, print_function, unicode_literals
from asyncio.windows_events import NULL
from unicodedata import decimal
from wolframclient.evaluation import WolframCloudSession
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AudioForm
import numpy as np
import wave
import struct

def binToDec(x):
    """ Call the API using function input parameter values.
    If the API was deployed with an export formats set to JSON or WXF, the result is often a native Python type.
    """
    with WolframCloudSession() as session:
        api_response = session.call('https://www.wolframcloud.com/obj/cae7dc50-b2d7-45bc-872d-3b4bd28f5523', {'x' : x})
        return api_response.get()


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
            # Some Useful Variables
            window_size = 2205    # Size of window to be used for detecting silence
            beta = 1   # Silence detection parameter
            max_notes = 100    # Maximum number of notes in file, for efficiency
            sampling_freq = 44100	# Sampling frequency of audio signal
            threshold = 600
            array = [10,
		     16.35160, 18.35405, 20.60172, 21.82676, 24.49971, 27.50000, 30.86771,
		     32.70320, 36.70810, 41.20344, 43.65353, 48.99943, 55.00000, 61.73541,
		    65.40639, 73.41619, 82.40689, 87.30706, 97.99886, 110.0000, 123.4708,
		    130.8128, 146.8324, 164.8138, 174.6141, 195.9977, 220.0000, 246.9417,
		    261.6256, 293.6648, 329.6276, 349.2282, 391.9954, 440.0000, 493.8833,
		    523.2511, 587.3295, 659.2551, 698.4565, 783.9909, 880.0000, 987.7666,
		    1046.502, 1174.659, 1318.510, 1396.913, 1567.982, 1760.000, 1975.533,
		    2093.005, 2349.318, 2637.020, 2793.826, 3135.963, 3520.000, 3951.066,
		    4186.009, 4698.636, 5274.041, 5587.652, 6271.927, 7040.000, 7902.133]

            notes = ['S',
		     'C0', 'D0', 'E0', 'F0', 'G0', 'A0', 'B0',
		     'C1', 'D1', 'E1', 'F1', 'G1', 'A1', 'B1',
		     'C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B2',
		     'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3',
		     'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4',
		     'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5',
		    'C6', 'D6', 'E6', 'F6', 'G6', 'A6', 'B6',
            'C7', 'D7', 'E7', 'F7', 'G7', 'A7', 'B7',
            'C8', 'D8', 'E8', 'F8', 'G8', 'A8', 'B8']

            binVals = ['000000',
		   '000001', '000010', '000011', '000100', '000101', '000110', '000111',
		   '001000', '001001', '001010', '001011', '001100', '001101', '001110',
		   '001111', '010000', '010001', '010010', '010011', '010100', '010101',
		   '010110', '010111', '011000', '011001', '011010', '011011', '011100',
		   '011101', '011110', '011111', '100000', '100001', '100010', '100011',
		   '100100', '100101', '100110', '100111', '101000', '101001', '101010',
		   '101011', '101100', '101101', '101110', '101111', '110000', '110001',
		   '110010', '110011', '110100', '110101', '110110', '110111', '111000',
		   '111001', '111010', '111011', '111100', '111101', '111110', '111111']

            Identified_Notes = []
            uploaded_file = request.FILES['record']
            newName = uploaded_file.name
            newName = newName.replace(" ", "_")
            sound_file = wave.open("static/audio/" + newName, 'r')
            file_length = sound_file.getnframes()

            sound = np.zeros(file_length)
            mean_square = []
            sound_square = np.zeros(file_length)
            for i in range(file_length):
                data = sound_file.readframes(1)
                data = struct.unpack("hh", data)
                sound[i] = int(data[0])
                
            sound = np.divide(sound, float(2**15))	# Normalize data in range -1 to 1


            ######################### DETECTING SCILENCE ##################################

            sound_square = np.square(sound)
            frequency = []
            dft = []
            i = 0
            j = 0
            k = 0    
            # traversing sound_square array with a fixed window_size
            while(i<=len(sound_square)-window_size):
                s = 0.0
                j = 0
                while(j<=window_size):
                    s = s + sound_square[i+j]
                    j = j + 1	
            # detecting the silence waves
                if s < threshold:
                    if(i-k>window_size*4):
                        dft = np.array(dft) # applying fourier transform function
                        dft = np.fft.fft(sound[k:i])
                        dft=np.argsort(dft)

                        if(dft[0]>dft[-1] and dft[1]>dft[-1]):
                            i_max = dft[-1]
                        elif(dft[1]>dft[0] and dft[-1]>dft[0]):
                            i_max = dft[0]
                        else :	
                            i_max = dft[1]
            # claculating frequency				
                        frequency.append((i_max*sampling_freq)/(i-k))
                        dft = []
                        k = i+1
                i = i + window_size

            #print('length',len(frequency))
            #print("frequency")   

            for i in frequency :
                print(i)
                idx = (np.abs(array-i)).argmin()
                Identified_Notes.append(notes[idx])
            print(Identified_Notes)
            binKey=''
            for curNote in Identified_Notes[:171]:
	            binKey+=binVals[notes.index(curNote)]

            binKey = binKey[:-3]+'1'
            decimalNum = binToDec(binKey)
            decimalNum = decimalNum.decode('UTF-8')
            print(decimalNum)
            newDecimalNum = ''
            while len(decimalNum) > 0:
                if len(decimalNum) < 100:
                    newDecimalNum = newDecimalNum + decimalNum[0:] + ' '
                    decimalNum=''
                else:
                    newDecimalNum = newDecimalNum + decimalNum[0:100] + ' '
                    decimalNum = decimalNum[100:]
            print(newDecimalNum)
            isPrime=call(binKey)
            isPrime=isPrime.decode('UTF-8')
            print(isPrime)
            print(decimalNum)
            context = {'form': form, 'isPrime':isPrime, 'decimalNum': newDecimalNum}
            return render(request, 'gen-primes.html', context)
    isPrime = False
    decimalNum = 0
    context = {'form': form, 'isPrime':isPrime, 'decimalNum': decimalNum}
    return render(request, 'gen-primes.html', context)

def piano(request):
    context = {}
    return render(request, 'piano.html', context)
