from django.db.models import manager
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Customers
from .serializers import CustomersSerializers



class CustomersAll(APIView):
    def get(self, request, *args, **kwargs ):
        qs = Customers.objects.all()
        customer_serializer = CustomersSerializers(qs, many=True)
        return Response(customer_serializer.data)


class CustomerByID(APIView):
    def get(self, request, *args, **kwargs):
        qs = Customers.objects.get(id=kwargs['customer_id'])
        customer_serializer = CustomersSerializers(qs)
        return Response(customer_serializer.data)