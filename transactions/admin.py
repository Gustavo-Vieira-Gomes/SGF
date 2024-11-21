from django.contrib import admin
from .models import TransactionCategory, Transaction


@admin.register(TransactionCategory)
class TransactionCategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'transaction_type',)
    search_fields = ('category', 'transaction_type',)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('value', 'description', 'bank_account', 'transaction_type', 'transaction_category', 'cost_center', 'supplier', 'client', 'creation_date', 'transaction_date', 'updated_at', 'company_associated')
    search_fields = ('value', 'description', 'bank_account', 'transaction_type', 'transaction_category', 'cost_center', 'supplier', 'client', 'creation_date', 'transaction_date', 'company_associated')
