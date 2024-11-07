from django.views import generic
from django.urls import reverse_lazy
from .models import Client
from .forms import ClientForm
from authentication.models import UserCompany
from django.shortcuts import redirect


class ClientListView(generic.ListView):
    model = Client
    template_name = 'client_list.html'
    context_object_name = 'clients'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('client_name')

        if name:
            queryset = queryset.filter(client_name__icontains=name)

        return queryset


class ClientCreateView(generic.CreateView):
    model = Client
    template_name = 'client_create.html'
    form_class = ClientForm
    success_url = reverse_lazy('client_list')

    def form_valid(self, form):
        client = form.save(commit=False)
        try:
            user_company = UserCompany.objects.get(user=self.request.user)
            client.client_company = user_company.company
            client.save()
            return redirect(self.success_url)
        except UserCompany.DoesNotExist:
            form.add_error(None, 'Usuário não está associado a nenhuma empresa.')
            return self.form_invalid(form)


class ClientDetailView(generic.DetailView):
    model = Client
    template_name = 'client_detail.html'
 

class ClientUpdateView(generic.UpdateView):
    model = Client
    template_name = 'client_update.html'
    form_class = ClientForm
    success_url = reverse_lazy('client_list')


class ClientDeleteView(generic.DeleteView):
    model = Client
    template_name = 'client_delete.html'
    success_url = reverse_lazy('client_list')
