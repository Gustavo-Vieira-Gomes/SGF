from django.contrib import admin
from .models import Supplier


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('supplier_name', 'supplier_cnpj', 'supplier_phone_number', 'supplier_company')
    search_fields = ('supplier_name', 'supplier_cnpj', 'supplier_cnpj',)
