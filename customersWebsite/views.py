from django.shortcuts import render
import requests
from django.urls import reverse

# Create your views here.

def index(request):
    if request.GET.get("submit"):
        customer_id = request.GET["customer_id"]
        if customer_id:
            url = 'http://127.0.0.1:8000' + reverse('customer_id', kwargs={'customer_id':customer_id}) 
            r = requests.get( url )
            return render(request, 'index.html', {'data': r.json(), 'search_type': 'show_by_id'} ) 
   
    if request.GET.get("show_all"):
        url = 'http://127.0.0.1:8000' + reverse('customer_all')
        r = requests.get( url )
        return render(request, 'index.html', {'data': r.json(), 'search_type': 'show_all'} ) 
    
    
    return render(request, 'index.html', {'data': ''} ) 