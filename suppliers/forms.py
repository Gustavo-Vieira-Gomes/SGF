from django import forms
from .models import Supplier



class SupplierForm(forms.ModelForm):

    class Meta:
        model = Supplier
        fields = ['supplier_name', 'supplier_cnpj', 'supplier_phone_number']

        widgets = {
            'supplier_name': forms.TextInput(attrs={'class': 'form-control'}),
            'supplier_cnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'supplier_phone_number': forms.TextInput(attrs={'class': 'form-control'})
        }

        labels = {
            'supplier_name': 'Nome do Fornecedor',
            'supplier_cnpj': 'CNPJ do Fornecedor',
            'supplier_phone_number': 'Número de Telefone do Fornecedor' 
        }
