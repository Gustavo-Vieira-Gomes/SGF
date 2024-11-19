from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clients.urls')),
    path('', include('suppliers.urls')),
    path('', include('bank_accounts.urls')),
    path('', include('companies.urls')),
    path('', include('transactions.urls'))
]
