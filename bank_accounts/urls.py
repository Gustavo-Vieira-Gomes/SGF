from django.urls import path
from .views import BankAccountListView, BankAccountCreateView, BankAccountDetailView, BankAccountUpdateView, BankAccountDeleteView


urlpatterns = [
    path('bank_accounts/list/', BankAccountListView.as_view(), name='bank_account_list'),
    path('bank_accounts/create/', BankAccountCreateView.as_view(), name='bank_account_create'),
    path('bank_accounts/detail/<int:pk>/', BankAccountDetailView.as_view(), name='bank_account_detail'),
    path('bank_accounts/update/<int:pk>/', BankAccountUpdateView.as_view(), name='bank_account_update'),
    path('bank_accounts/delete/<int:pk>/', BankAccountDeleteView.as_view(), name='bank_account_delete')
]
