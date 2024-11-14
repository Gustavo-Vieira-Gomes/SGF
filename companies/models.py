from django.db import models


class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(verbose_name='Nome da Empresa', max_length=30, unique=True)
    cnpj = models.CharField(verbose_name='CNPJ da empresa', max_length=14, blank=True, null=True, unique=True)
    company_address = models.TextField(verbose_name='Endereço da Empresa', blank=True, null=True)
    phone = models.CharField(verbose_name='Telefone da Empresa', max_length=11)
    email = models.EmailField(verbose_name='Email da empresa', unique=True)
    updated_at = models.DateTimeField(verbose_name='Data da última alteração', auto_now=True)
    created_at = models.DateTimeField(verbose_name='Data de cadastro da empresa', auto_now_add=True)

    def __str__(self):
        return self.name
    

class CostCenter(models.Model):
    name = models.CharField(verbose_name='Nome do Centro de Custo', max_length=100, unique=True)
    description = models.TextField(verbose_name='Descrição do Centro de Custo e suas atribuições', blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Compania Associada')

    class Meta:
        ordering = ['name']
        verbose_name = 'Centros de Custo'

    def __str__(self):
        return self.name
