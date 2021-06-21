from django.core.management.base import BaseCommand
from customerDetailsApi.models import Customers
import pandas as pd
from tqdm import tqdm
from ...utils import get_lat_long


class Command(BaseCommand):
    '''Class to create custom command importcustomerdetails'''

    def add_arguments(self, parser):
        '''Adding required commandline argument file_path'''

        parser.add_argument(
            'file_path',
            type=str,
            help="File path to import"
        )

    def handle(self, *args, **kwargs):
        '''Handles the command

        Takes csv file path, reads the csv, 
        Iterate over the data
        Retrieves latitude, longitude using customer address
        Creates a list of customer objects 
        Saves the list in database using bulk_create
        '''

        file_path = kwargs['file_path']
        customers = []
        customer_data = pd.read_csv(file_path)

        # create a new Customer model class object for each row in .csv file
        for i, row in tqdm(customer_data.iterrows()):
            lat, lng = get_lat_long(row['city'])

            customers.append(
                Customers(
                  first_name=row['first_name'],
                  last_name=row['last_name'],
                  email=row['email'],
                  gender=row['gender'],
                  city=row['city'],
                  company=row['company'],
                  title=row['title'],
                  lat=lat,
                  lng=lng,
                )

            )

        Customers.objects.bulk_create(customers)  # Insert into database.
