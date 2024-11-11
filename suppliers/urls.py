from django.urls import path
from .views import SupplierListView, SupplierCreateView, SupplierDetailView, SupplierUpdateView, SupplierDeleteView


urlpatterns = [
    path('suppliers/list/', SupplierListView.as_view(), name='supplier_list'),
    path('suppliers/create/', SupplierCreateView.as_view(), name='supplier_create'),
    path('suppliers/detail/<int:pk>/', SupplierDetailView.as_view(), name='supplier_detail'),
    path('suppliers/update/<int:pk>/', SupplierUpdateView.as_view(), name='supplier_update'),
    path('suppliers/delete/<int:pk>/', SupplierDeleteView.as_view(), name='supplier_delete'),
]
