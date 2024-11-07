from django.contrib import admin
from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'cnpj', 'company_address', 'phone', 'email', 'updated_at', 'created_at')
    search_fields = ('name', 'cnpj', )
