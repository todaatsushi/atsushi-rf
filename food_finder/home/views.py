from django.shortcuts import render

import pandas as pd

# Load stations data
from .get_stations import stations
from .forms import QueryForm

# Zomato API configure
from pyzomato import Pyzomato
from secret import ZOMATO_API_KEY


def home_page(request):

    if request.method == 'POST':
        context = {}

        stop= request.POST.get('stop', 'NONE')
        func = request.POST.get('type', 'NONE')

        return render(request, 'home/result.html', context=context)

    else:
        # Log into API
        context = {
            'stations': stations,
            'names': stations['Name'],
        }

        return render(request, 'home/home.html', context=context)
