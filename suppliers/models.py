from django.db import models
from companies.models import Company


class Supplier(models.Model):
    supplier_name = models.CharField(verbose_name='Nome do Fornecedor', max_length=80, unique=True)
    supplier_cnpj = models.CharField(verbose_name='CNPJ do Fornecedor', max_length=14, unique=True, blank=True, null=True)
    supplier_phone_number = models.CharField(verbose_name='Telefone do Fornecedor', max_length=11, unique=True)
    supplier_company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Empresa da qual é Fornecedor')
    created_at = models.DateTimeField(verbose_name='Data de Criação' ,auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Data da Última Alteração', auto_now=True)

    class Meta:
        ordering = ['supplier_name']

    def __str__(self):
        return self.supplier_name
