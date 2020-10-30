from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserInput
from rest_framework import status
from rest_framework.response import Response
import requests

def get_code(request):

    if request.method == 'POST':
        form = UserInput(request.POST)
        user_code = request.POST.get('userCode')
        user_input = request.POST.get('customInput')
        RUN_URL = "https://api.hackerearth.com/v3/code/run/"
        CLIENT_SECRET = 'e49c515d316b8d5d1e5bda7a323e3ce2f2766d5b'

        if form.is_valid():
            code  = """{code0}""".format(code0=user_code)
            Input = """{input0}""".format(input0=user_input)
            data = {
                'client_secret': CLIENT_SECRET,
                'async': 0,
                'source': code,
                'input': Input,
                'lang': 'PYTHON3',
                'time_limit': 5
            }
            print("Calling API")
            r = requests.post(RUN_URL, data=data).json()
            print("API Called...")
            output_data = {
                'output': r['run_status']['output'],
                'output_html': r['run_status']['output_html'],
                'time': r['run_status']['time_used'],
                'memory': r['run_status']['memory_used'],
                'error': r['run_status']['stderr'],
            }
            print(output_data)
            context = {'output_data': output_data,
            'form': UserInput(),
            }
            return render(request, 'compiler2.html', context=context)
        
    
    else:
        form = UserInput()

    return render(request, 'compiler2.html', {'form': form})