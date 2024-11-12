from django import forms
from .models import BankAccount


class BankAccountForm(forms.ModelForm):

    class Meta:
        model = BankAccount
        fields = ['bank', 'account_balance', 'agency_number', 'account_number', 'account_type']

        widgets = {
            'bank': forms.TextInput(attrs={'class': 'form-control'}),
            'account_balance': forms.NumberInput(attrs={'class': 'form-control'}),
            'agency_number': forms.TextInput(attrs={'class': 'form-control'}),
            'account_number': forms.TextInput(attrs={'class': 'form-control'}),
            'account_type': forms.Select(attrs={'class': 'form-control'})
        }

        labels = {
            'bank': 'Instituição/Banco',
            'account_balance': 'Saldo Da Conta',
            'agency_number': 'Número da Agência da Conta',
            'account_number': 'Número da Conta',
            'account_type': 'Tipo de Conta'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields.pop('campo_apenas_para_criacao')
