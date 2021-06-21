from django.urls import path
from customerDetailsApi.views import CustomersAll
from customerDetailsApi.views import CustomerByID

urlpatterns = [
    path('all/', CustomersAll.as_view(), name="customer_all"),
    path('<int:customer_id>/', CustomerByID.as_view(), name="customer_id"),
]
