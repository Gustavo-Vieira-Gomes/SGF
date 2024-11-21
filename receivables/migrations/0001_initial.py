# Generated by Django 5.1.3 on 2024-11-21 15:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
        ('bank_accounts', '0002_bankaccount_created_at_bankaccount_updated_at'),
        ('clients', '0002_client_created_at_client_updated_at'),
        ('companies', '0002_costcenter'),
        ('transactions', '0002_transaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receivable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(verbose_name='Valor a Receber')),
                ('description', models.TextField(verbose_name='Descrição do Valor')),
                ('registration_date', models.DateTimeField(auto_now_add=True, verbose_name='Data de registro da conta a receber')),
                ('due_date', models.DateField(verbose_name='Data de Vencimento')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Última Alteração:')),
                ('bank_account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bank_accounts.bankaccount', verbose_name='Conta bancária utilizada para receber')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clients.client', verbose_name='Cliente responsável pela entrada')),
                ('company_associated', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.usercompany', verbose_name='Compania envolvida')),
                ('cost_center', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='companies.costcenter', verbose_name='Centro de Custo associado')),
                ('transaction_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='transactions.transactioncategory', verbose_name='Categoria da Operação')),
            ],
            options={
                'verbose_name': 'Contas a Receber',
                'ordering': ['-due_date', '-value'],
            },
        ),
    ]