from django.db import models
from companies.models import Company


class BankAccount(models.Model):

    class AccountType(models.TextChoices):
        CONTA_CORRENTE = 'CC', 'Conta Corrente'
        CONTA_POUPANCA = 'CP', 'Conta Poupança'
        CONTA_PAGAMENTO = 'CPG', 'Conta Pagamento'
        CONTA_INVESTIMENTO = 'CI', 'Conta de Investimentos'
        CONTA_EMPRESARIAL = 'CE', 'Conta Empresarial'

    bank = models.CharField(verbose_name='Nome do Banco', max_length=50)
    account_balance = models.FloatField(verbose_name='Saldo da Conta', default=0)
    agency_number = models.CharField(verbose_name='Número da Agência Bancária', max_length=4)
    account_number = models.CharField(verbose_name='Número da Conta', max_length=20)
    account_type = models.CharField(verbose_name='Tipo de conta bancária', max_length=60, choices=AccountType.choices, default=AccountType.CONTA_EMPRESARIAL)
    account_company = models.ForeignKey(verbose_name='Empresa proprietária da conta', to=Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['bank']
        verbose_name = 'Contas Bancárias'

    def __str__(self):
        return self.bank
