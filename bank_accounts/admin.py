from django.contrib import admin
from .models import BankAccount


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('bank', 'agency_number', 'account_number', 'account_type', 'account_balance', 'account_company')
    search_fields = ('bank', 'agency_number', 'account_number', 'account_type', 'account_company')
