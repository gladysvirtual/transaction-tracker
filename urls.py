from django.urls import path
from .views import home, login, transactions_monitoring, transaction_list

urlpatterns = [
    path('', home),
    path('login/', login, name='login'),
    path('transactions/', transaction_list, name='transactions'),
    path('transactions /', transactions_monitoring),
]
