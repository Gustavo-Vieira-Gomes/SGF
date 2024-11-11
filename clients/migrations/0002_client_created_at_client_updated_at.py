# Generated by Django 5.1.3 on 2024-11-07 01:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 11, 6, 22, 56, 29, 779958), verbose_name='Data de Criação'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Data da Última Alteração'),
        ),
    ]