from django.views import generic
from .models import CostCenter
from .forms import CostCenterForm
from authentication.models import UserCompany
from django.shortcuts import redirect
from django.urls import reverse_lazy


class CostCenterListView(generic.ListView):
    model = CostCenter
    template_name = 'cost_center_list.html'
    context_object_name = 'cost_centers'

    def get_queryset(self):
        queryset = super().get_queryset()

        description = self.request.GET.get('description')

        if description:
            queryset = queryset.filter(description__icontains=description)
        
        return queryset


class CostCenterCreateView(generic.CreateView):
    model = CostCenter
    template_name = 'cost_center_create.html'
    form_class = CostCenterForm
    success_url = reverse_lazy('cost_center_list')

    def form_valid(self, form):
        cost_center = form.save(commit=False)
        try:
            user_company = UserCompany.objects.get(user=self.request.user)
            cost_center.company = user_company.company
            cost_center.save()
            return redirect(self.success_url)
        except UserCompany.DoesNotExist:
            form.add_error(None, 'Usuário não está associado a nenhuma empresa.')
            return self.form_invalid(form)


class CostCenterDeleteView(generic.DeleteView):
    model = CostCenter
    template_name = 'cost_center_delete.html'
    success_url = reverse_lazy('cost_center_list')
