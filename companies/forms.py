from django import forms
from .models import CostCenter


class CostCenterForm(forms.ModelForm):

    class Meta:
        model = CostCenter
        fields = ['name', 'description']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'})
        }

        labels = {
            'name': 'Nome do Centro de Custo',
            'description': 'Descrição do Centro de Custo e suas Atribuições'
        }
