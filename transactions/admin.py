from django.contrib import admin
from .models import TransactionCategory


@admin.register(TransactionCategory)
class TransactionCategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'transaction_type',)
    search_fields = ('category', 'transaction_type',)
