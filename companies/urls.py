from django.urls import path
from .views import CostCenterListView, CostCenterCreateView, CostCenterDeleteView


urlpatterns = [
    path('companies/cost_centers/list/', CostCenterListView.as_view(), name='cost_center_list'),
    path('companies/cost_centers/create/', CostCenterCreateView.as_view(), name='cost_center_create'),
    path('companies/cost_centers/delete/<int:pk>/', CostCenterDeleteView.as_view(), name='cost_center_delete'),
]
