from django.urls import path
from .views import ClientListView, ClientCreateView, ClientDetailView, ClientUpdateView, ClientDeleteView


urlpatterns = [
    path('clients/list/', ClientListView.as_view(), name='client_list'),
    path('clients/create/', ClientCreateView.as_view(), name='client_create'),
    path('clients/detail/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('clients/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('clients/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
]
