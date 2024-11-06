from django.views import generic
from django.urls import reverse_lazy
from .models import Client


class ClientListView(generic.ListView):
    model = Client
    template_name = 'client_list.html'
    context_object_name = 'clients'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')
        
        if name:
            queryset = queryset.filter(name__icontains=name)
        
        return queryset


class ClientCreateView(generic.CreateView):
    model = Client
    template_name = 'client_create.html'
    form_class = ...
    success_url = reverse_lazy('client_list')


class ClientDetailView(generic.DetailView):
    model = Client
    template_name = 'client_detail.html'


class ClientUpdateView(generic.UpdateView):
    model = Client
    template_name = 'client_update.html'
    form_class = ...
    success_url = reverse_lazy('client_list')


class BrandDeleteView(generic.DeleteView):
    model = Client
    template_name = 'client_delete.html'
    success_url = reverse_lazy('client_list')
