from django.core.management.base import BaseCommand
from customerDetailsApi.models import Customers
import pandas as pd
from ...utils import get_lat_long

from tqdm import tqdm


class Command(BaseCommand):

    def add_arguments(self, parser):
            parser.add_argument('file_path', type=str, help="File path to import")


    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path'] #postional argument
        customers = []
        customer_data = pd.read_csv( file_path ) # read customer data from customers.csv
        
        # create a new Customer model class object for each row in .csv file
        for i, row in tqdm(customer_data.iterrows()):
            lat, lng = get_lat_long(row['city'])
            customers.append(
                Customers(
                  first_name = row['first_name'],
                  last_name  = row['last_name'],
                  email      = row['email'],
                  gender     = row['gender'],
                  city       = row['city'],
                  company    = row['company'],
                  title      = row['title'],
                  lat        = lat,
                  lng        = lng,
                )
            )
        
        Customers.objects.bulk_create(customers) # insert into database.