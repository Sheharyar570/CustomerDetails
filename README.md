# Customer Details API and Web Page to Consume it.

A Django REST API with two endpoints. Can get customers data using the API. 
- customer/<customer_id> endpoint returns single customer details.
- customer/all endpoint returns all customer details.

A Simple Web page is created to consume the API.

### Docker Installation Instruction.
- Download zip or clone this repository.
- Extract the zip to the folder (In case: Repo was downloaded)
- Got the folder where you have extracted the downloaded file.
- Place your Google Maps API key in CustomerDetails/settings.py at line 140

```
GOOGLE_MAPS_API_KEY = 'PLACE_YOUR_API_KEY_HERE'
```

- Open cmd and run the below commands in sequence.

```
docker-compose build
```

```
docker-compose run web python manage.py migrate
```

```
docker-compose run web python manage.py importcustomerdetails customers.csv
```

```
docker-compose up
```
### Installation Instruction.
- Install python3.9 and pip 
- Install postgres and setup postgres with default username and password=admin123
- Download zip or clone this repository.
- Extract the zip to the folder (In case: Repo was downloaded)
- Go to the folder where you have extracted the downloaded file.
- Place your Google Maps API key in CustomerDetails/settings.py at line 140

```
GOOGLE_MAPS_API_KEY = 'PLACE_YOUR_API_KEY_HERE'
```

- Change CustomerDetails/settings.py file

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'customers',
        'USER': 'postgres',
        'HOST': 'db',
        'PASSWORD': 'mustard@846#',
        'PORT': '5432'
    }
}
```

TO

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'customers',
        'USER': 'postgres',
        'HOST': 'localhost',
        'PASSWORD': 'admin123',
        'PORT': '5432'
    }
}

```

- Open cmd and run the below commands in sequence.


```
pip install -r requirements.txt
```

```
python manage.py migrate
```

```
python manage.py importcustomerdetails customers.csv
```
```
python manage.py runserver
```
