from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Customers
from .serializers import CustomersSerializers


class CustomersAll(APIView):
    def get(self, request, *args, **kwargs):
        '''API endpoint retreives customers from database and returns the response'''

        try:
            query_set = Customers.objects.all()
        except Customers.DoesNotExist:
            query_set = None

        customer_serializer = CustomersSerializers(query_set, many=True)
        return Response(customer_serializer.data)


class CustomerByID(APIView):
    def get(self, request, *args, **kwargs):
        '''API endpoint retreives customer using customer_id 
        from database and returns the response
        '''

        try:
            query_set = Customers.objects.get(id=kwargs['customer_id'])
        except Customers.DoesNotExist:
            query_set = None

        customer_serializer = CustomersSerializers(query_set)
        return Response(customer_serializer.data)
