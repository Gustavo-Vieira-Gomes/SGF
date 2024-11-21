from django import forms
from .models import Receivable
from transactions.models import TransactionCategory


class ReceivableForm(forms.ModelForm):

    class Meta:
        model = Receivable
        fields = ['description', 'value', 'bank_account', 'transaction_category', 'cost_center', 'client', 'due_date']

        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'value': forms.NumberInput(attrs={'class': 'form-control'}),
            'bank_account': forms.Select(attrs={'class': 'form-control'}),
            'transaction_category': forms.Select(attrs={'class': 'form-control'}),
            'cost_center': forms.Select(attrs={'class': 'form-control'}),
            'client':  forms.Select(attrs={'class': 'form-control'}),
            'due_date': forms.DateTimeInput(attrs={'class': 'form-control'})
        }
    
    def __init__(self, data = ..., files = ..., auto_id = ..., prefix = ..., initial = ..., error_class = ..., label_suffix = ..., empty_permitted = ..., instance = ..., use_required_attribute = ..., renderer = ...):
        super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, instance, use_required_attribute, renderer)
        self.fields['categoria'].queryset = TransactionCategory.objects.filter(transaction_type=1)
