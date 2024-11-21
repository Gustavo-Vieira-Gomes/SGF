from django.db import models
from bank_accounts.models import BankAccount
from transactions.models import TransactionCategory
from companies.models import CostCenter
from clients.models import Client
from authentication.models import UserCompany


class Receivable(models.Model):
    value = models.FloatField(verbose_name='Valor a Receber')
    description = models.TextField(verbose_name='Descrição do Valor')
    bank_account = models.ForeignKey(BankAccount, verbose_name='Conta bancária utilizada para receber', on_delete=models.PROTECT)
    transaction_category = models.ForeignKey(TransactionCategory, verbose_name='Categoria da Operação', on_delete=models.PROTECT, blank=True, null=True)
    cost_center = models.ForeignKey(CostCenter, verbose_name='Centro de Custo associado', on_delete=models.PROTECT)
    client = models.ForeignKey(Client, verbose_name='Cliente responsável pela entrada', on_delete=models.PROTECT, blank=True, null=True)
    registration_date = models.DateTimeField(verbose_name='Data de registro da conta a receber', auto_now_add=True)
    due_date = models.DateField(verbose_name='Data de Vencimento')
    updated_at = models.DateTimeField(verbose_name='Última Alteração:', auto_now=True)
    company_associated = models.ForeignKey(UserCompany, verbose_name='Compania envolvida', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-due_date', '-value']
        verbose_name = 'Contas a Receber'
    
    def __str__(self):
        return f'{self.value:.2f} - {self.description}'
