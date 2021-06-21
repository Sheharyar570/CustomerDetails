from django.db import models
from rest_framework import serializers

from .models import Customers

class CustomersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = (
            'id',
            'first_name', 
            'last_name', 
            'email',
            'gender',
            'company',
            'city',
            'title',
            'lng',
            'lat',
        )