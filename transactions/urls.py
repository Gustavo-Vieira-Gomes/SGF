from django.urls import path
from .views import TransactionCategoryListView, TransactionCategoryCreateView, TransactionCategoryDeleteView


urlpatterns = [
    path('transactions/categories/list/', TransactionCategoryListView.as_view(), name='transaction_category_list'),
    path('transactions/categories/create/', TransactionCategoryCreateView.as_view(), name='transaction_category_create'),
    path('transactions/categories/delete/<int:pk>/', TransactionCategoryDeleteView.as_view(), name='transaction_category_delete'),
]
