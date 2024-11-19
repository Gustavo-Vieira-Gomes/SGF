from django.views import generic
from .models import TransactionCategory
from .forms import TransactionCategoryForm
from authentication.models import UserCompany
from django.shortcuts import redirect
from django.urls import reverse_lazy


class TransactionCategoryListView(generic.ListView):
    model = TransactionCategory
    template_name = 'transaction_category_list.html'
    context_object_name= 'transaction_categories'

    def get_queryset(self):
        queryset = super().get_queryset()

        transaction_type = self.request.GET.get('transaction_type', '2')

        if transaction_type != '2':
            transaction_type = int(transaction_type)
            queryset = queryset.filter(transaction_type=transaction_type)
        
        return queryset


class TransactionCategoryCreateView(generic.CreateView):
    model = TransactionCategory
    template_name = 'transaction_category_create.html'
    form_class = TransactionCategoryForm
    success_url = reverse_lazy('transaction_category_list')

    def form_valid(self, form):
        transaction_category = form.save(commit=False)
        try:
            user_company = UserCompany.objects.get(user=self.request.user)
            transaction_category.account_company = user_company.company
            transaction_category.save()
            return redirect(self.success_url)
        except UserCompany.DoesNotExist:
            form.add_error(None, 'Usuário não está associado a nenhuma empresa.')
            return self.form_invalid(form)


class TransactionCategoryDeleteView(generic.DeleteView):
    model = TransactionCategory
    template_name = 'transaction_category_delete.html'
    success_url = reverse_lazy('transaction_category_list')
