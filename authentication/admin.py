from django.contrib import admin
from .models import UserCompany


@admin.register(UserCompany)
class UserCompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'company')
    search_fields = ('user', 'company')
