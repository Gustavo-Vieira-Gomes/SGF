from django.contrib import admin
from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_cnpj', 'client_phone_number', 'client_company')
    search_fields = ('client_name', 'client_cnpj', 'client_cnpj',)
