# Customer Details API and Web Page to Consume it.

A Django REST API with two endpoints. Can get customers data using the API. 
- customer/<customer_id> endpoint returns single customer details.
- customer/all endpoint returns all customer details.

A Simple Web page is created to consume the API.

### Docker Installation Instruction.
- Download zip or clone this repository.
- Extract the zip to the folder (In case: Repo was downloaded)
- Got the folder where you have extracted the downloaded file.
- Open cmd and run the below commands in sequence.

```
docker-compose build
docker-compose run web python manage.py migrate
docker-compose run web python manage.py importcustomerdetails customers.csv
docker-compose up
```
### Installation Instruction.
- Install python3.9 and pip 
- Install postgres and setup postgres with default username and password=admin123
- Download zip or clone this repository.
- Extract the zip to the folder (In case: Repo was downloaded)
- Got the folder where you have extracted the downloaded file.
- Open cmd and run the below commands in sequence.


```
python manage.py migrate

# Import customer data from csv
python manage.py manage.py importcustomerdetails customers.csv
```
