from django import forms
from .models import Client


class ClientForm(forms.ModelForm):
    
    class Meta:
        model = Client
        fields = ['client_name', 'client_cnpj', 'client_phone_number']
        