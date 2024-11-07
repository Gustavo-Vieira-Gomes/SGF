from django import forms
from .models import Client



class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ['client_name', 'client_cnpj', 'client_phone_number']

        widgets = {
            'client_name': forms.TextInput(attrs={'class': 'form-control'}),
            'client_cnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'client_phone_number': forms.TextInput(attrs={'class': 'form-control'})
        }

        labels = {
            'client_name': 'Nome do Cliente',
            'client_cnpj': 'CNPJ do Cliente',
            'client_phone_number': 'Número de Telefone do Cliente' 
        }