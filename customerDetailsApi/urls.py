from django.urls import path
from customerDetailsApi.views import CustomersAll
from customerDetailsApi.views import CustomerByID

urlpatterns = [
    path('all/', CustomersAll.as_view(), name="customer_all" ), # url for displaying all customers data
    path('<int:customer_id>/', CustomerByID.as_view(), name="customer_id") # url to display customers data based on customer id. Customer id passed as url parameter.
]