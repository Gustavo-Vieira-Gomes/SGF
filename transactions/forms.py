from django import forms
from .models import TransactionCategory


class TransactionCategoryForm(forms.ModelForm):

    class Meta:
        model = TransactionCategory
        fields = '__all__'

        widgets = {
            'category':  forms.TextInput(attrs={'class': 'form-control'}),
            'transaction_type': forms.Select(attrs={'class': 'form-control'})
        }

        labels = {
            'category': 'Nome da Categoria',
            'transaction_type': 'Tipo de Transação'
        }

