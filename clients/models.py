from django.db import models
from companies.models import Company


class Client(models.Model):
    id = models.IntegerField(primary_key=True)
    client_name = models.CharField(verbose_name='Nome do Cliente', max_length=80, unique=True)
    client_cnpj = models.CharField(verbose_name='CNPJ do Cliente', max_length=14, unique=True)
    client_phone_number = models.CharField(verbose_name='Telefone do Cliente', max_length=11, unique=True)
    client_company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Empresa da qual é cliente')

    class Meta:
        ordering = ['client_name']

    def __str__(self):
        return self.client_name
