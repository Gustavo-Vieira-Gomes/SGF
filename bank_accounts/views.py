from django.views import generic
from django.urls import reverse_lazy
from .models import BankAccount
from .forms import BankAccountForm
from authentication.models import UserCompany
from django.shortcuts import redirect


class BankAccountListView(generic.ListView):
    model = BankAccount
    template_name = 'bank_account_list.html'
    context_object_name = 'bank_accounts'

    def get_queryset(self):
        queryset = super().get_queryset()

        bank = self.request.GET.get('bank')

        if bank:
            queryset = queryset.filter(bank__icontains=bank)
        
        return queryset


class BankAccountCreateView(generic.CreateView):
    model = BankAccount
    template_name = 'bank_account_create.html'
    form_class = BankAccountForm
    success_url = reverse_lazy('bank_account_list')

    def form_valid(self, form):
        bank_account = form.save(commit=False)
        try:
            user_company = UserCompany.objects.get(user=self.request.user)
            bank_account.account_company = user_company.company
            bank_account.save()
            return redirect(self.success_url)
        except UserCompany.DoesNotExist:
            form.add_error(None, 'Usuário não está associado a nenhuma empresa.')
            return self.form_invalid(form)


class BankAccountDetailView(generic.DetailView):
    model = BankAccount
    template_name = 'bank_account_detail.html'


class BankAccountUpdateView(generic.UpdateView):
    model = BankAccount
    template_name = 'bank_account_update.html'
    form_class = BankAccountForm
    success_url = reverse_lazy('bank_account_list')


class BankAccountDeleteView(generic.DeleteView):
    model = BankAccount
    template_name = 'bank_account_delete.html'
    success_url  = reverse_lazy('bank_account_list')
