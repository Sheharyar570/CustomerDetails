from django.core.management.base import BaseCommand
from CustomerDetails.settings import BASE_DIR
from customerDetailsApi.models import Customers
import pandas as pd
import os

class Command(BaseCommand):

    def add_arguments(self, parser):
            parser.add_argument('file_path', type=str, help="File path to import")


    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path'] #postional argument
        customers = []
        customer_data = pd.read_csv( file_path ) # read customer data from customers.csv
       
        
        # create a new Customer model class object for each row in .csv file
        for i in range(0, customer_data.shape[0]):
            customers.append(
                Customers(
                  first_name = customer_data.iloc[i]['first_name'],
                  last_name  = customer_data.iloc[i]['last_name'],
                  email      = customer_data.iloc[i]['email'],
                  gender     = customer_data.iloc[i]['gender'],
                  city       = customer_data.iloc[i]['city'],
                  company    = customer_data.iloc[i]['company'],
                  title      = customer_data.iloc[i]['title'],
                )
            )
        
        Customers.objects.bulk_create(customers) # insert into database.