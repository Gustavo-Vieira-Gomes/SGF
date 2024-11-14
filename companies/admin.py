from django.contrib import admin
from .models import Company, CostCenter


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'cnpj', 'company_address', 'phone', 'email', 'updated_at', 'created_at')
    search_fields = ('name', 'cnpj', )


@admin.register(CostCenter)
class CostCenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
