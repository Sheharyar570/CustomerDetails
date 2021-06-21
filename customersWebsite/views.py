from django.http import response
from django.shortcuts import render
import requests
from django.urls import reverse


def index(request):
    '''Get user data from Customer API and render front-end.'''
    
    if request.GET.get("submit"):
        customer_id = request.GET["customer_id"]

        if customer_id:
            url = 'http://127.0.0.1:8000'
            url += reverse('customer_id', kwargs={'customer_id': customer_id})
            response = requests.get(url)

            data_json = {'data': response.json(), 'search_type': 'show_by_id'}
            return render(request, 'index.html', data_json)

    if request.GET.get("show_all"):
        url = 'http://127.0.0.1:8000' + reverse('customer_all')
        response = requests.get(url)

        data_json = {'data': response.json(), 'search_type': 'show_all'}
        return render(request, 'index.html', data_json)

    return render(request, 'index.html', {'data': ''})
