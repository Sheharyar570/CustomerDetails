from django.core.management.base import BaseCommand
from CustomerDetails.settings import BASE_DIR
from customerDetailsApi.models import Customers
import pandas as pd
import os

class Command(BaseCommand):

    def handle(self, *args, **options):
        customers = []
        customer_data = pd.read_csv(os.path.join( BASE_DIR, 'customers.csv' ) ) # read customer data from customers.csv

        # create a new Customer model class object for each row in customers.csv
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