from django.views import generic
from django.urls import reverse_lazy
from .models import Supplier
from .forms import SupplierForm
from authentication.models import UserCompany
from django.shortcuts import redirect


class SupplierListView(generic.ListView):
    model = Supplier
    template_name = 'supplier_list.html'
    context_object_name = 'suppliers'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('supplier_name')

        if name:
            queryset = queryset.filter(supplier_name__icontains=name)

        return queryset


class SupplierCreateView(generic.CreateView):
    model = Supplier
    template_name = 'supplier_create.html'
    form_class = SupplierForm
    success_url = reverse_lazy('supplier_list')

    def form_valid(self, form):
        supplier = form.save(commit=False)
        try:
            user_company = UserCompany.objects.get(user=self.request.user)
            supplier.supplier_company = user_company.company
            supplier.save()
            return redirect(self.success_url)
        except UserCompany.DoesNotExist:
            form.add_error(None, 'Usuário não está associado a nenhuma empresa.')
            return self.form_invalid(form)


class SupplierDetailView(generic.DetailView):
    model = Supplier
    template_name = 'supplier_detail.html'
 

class SupplierUpdateView(generic.UpdateView):
    model = Supplier
    template_name = 'supplier_update.html'
    form_class = SupplierForm
    success_url = reverse_lazy('supplier_list')


class SupplierDeleteView(generic.DeleteView):
    model = Supplier
    template_name = 'supplier_delete.html'
    success_url = reverse_lazy('supplier_list')
