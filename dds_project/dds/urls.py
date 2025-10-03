from django.urls import path
from .views import transaction_list, transaction_create, transaction_edit, transaction_delete

urlpatterns = [
    path('', transaction_list, name='transaction_list'),
    path('create/', transaction_create, name='transaction_create'),
    path('edit/<int:pk>/', transaction_edit, name='transaction_edit'),
    path('delete/<int:pk>/', transaction_delete, name='transaction_delete'),
]
