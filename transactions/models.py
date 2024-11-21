from django.db import models
from bank_accounts.models import BankAccount
from companies.models import CostCenter
from suppliers.models import Supplier
from clients.models import Client
from authentication.models import UserCompany


class TransactionCategory(models.Model):

    class TransactionType(models.IntegerChoices):
        SAÍDA = 0, 'Saída'
        ENTRADA = 1, 'Entrada'
    
    category = models.CharField('Nome da Categoria', max_length=50, unique=True)
    transaction_type = models.IntegerField('Tipo de Categoria', choices=TransactionType.choices, default=TransactionType.ENTRADA)

    def __str__(self):
        return self.category


class Transaction(models.Model):

    class TransactionType(models.IntegerChoices):
        SAÍDA = 0, 'Saída'
        ENTRADA = 1, 'Entrada'

    value = models.FloatField(verbose_name='Valor da Transação')
    description = models.TextField(verbose_name='Descrição da Transação', blank=True, null=True)
    bank_account = models.ForeignKey(BankAccount, verbose_name='Conta bancária utilizada para a transação', on_delete=models.PROTECT)
    transaction_type = models.IntegerField('Tipo de Categoria', choices=TransactionType.choices, default=TransactionType.ENTRADA)
    transaction_category = models.ForeignKey(TransactionCategory, verbose_name='Categoria da Transação', on_delete=models.PROTECT, blank=True, null=True)
    cost_center = models.ForeignKey(CostCenter, verbose_name='Centro de Custo envolvido na Transação', on_delete=models.PROTECT)
    supplier = models.ForeignKey(Supplier, verbose_name='Fornecedor envolvido na Transação', on_delete=models.PROTECT, blank=True, null=True)
    client = models.ForeignKey(Client, verbose_name='Cliente envolvido na Transação', on_delete=models.PROTECT, blank=True, null=True)
    creation_date = models.DateTimeField(verbose_name='Data de Criação da Transação no sistema a pagar ou a receber')
    transaction_date = models.DateTimeField(verbose_name='Data da Operação', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Data da última atualização', auto_now=True)
    company_associated = models.ForeignKey(UserCompany, verbose_name='Compania envolvida', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.value:.2f} - {self.description}'
