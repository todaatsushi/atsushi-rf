from django.shortcuts import render

import pandas as pd
from random import sample

# Load stations data
from .helper import stations, zomato, categories


def home_page(request):

    if request.method == 'POST':
        context = {}

        stop = request.POST.get('stop', 'NONE')
        func = request.POST.get('type', 'NONE')

        print(stop, func)

        # Get Lat/LNG from df with form data
        stop_info = stations[stations.Name == stop]
        lat = float(stop_info.iloc[0, 0])
        lng = float(stop_info.iloc[0, 1])

        context['info'] = [stop, lat, lng]

        # Get API data
        results = zomato.getByGeocode(lat, lng)

        results = [results['location']['entity_id'], results['location']['entity_type']]

        # Search test
        search1 = zomato.search(
            entity_id=results[0],
            entity_type=results[1],
            count=50,
            category=func,
            sort='real_distance',
        )

        search2 = zomato.search(
            entity_id=results[0],
            entity_type=results[1],
            count=50,
            category=func,
            sort='rating',
        )

        search1 = [[r['restaurant']['name'], 
                    r['restaurant']['user_rating']['aggregate_rating'], 
                    r['restaurant']['R']['res_id'],
                    r['restaurant']['url']] 
                    for r in search1['restaurants']
                    if float(r['restaurant']['user_rating']['aggregate_rating']) >= 3
                        or
                    float(r['restaurant']['user_rating']['aggregate_rating']) == 0]
        
        search2 = [[r['restaurant']['name'], 
                    r['restaurant']['user_rating']['aggregate_rating'], 
                    r['restaurant']['R']['res_id'],
                    r['restaurant']['url']] 
                    for r in search2['restaurants']]

        intersection = [r for r in search1 if r in search2]
        
        context['search'] = sample(intersection, 1)

        return render(request, 'home/result.html', context=context)

    else:
        context = {}
        context['categories'] = categories
        context['stations'] = stations
        context['names'] = stations['Name']

        return render(request, 'home/home.html', context=context)
