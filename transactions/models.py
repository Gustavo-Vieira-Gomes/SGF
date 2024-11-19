from django.db import models


class TransactionCategory(models.Model):
    
    class TransactionType(models.IntegerChoices):
        SAÍDA = 0, 'Saída'
        ENTRADA = 1, 'Entrada'
    
    category = models.CharField('Nome da Categoria', max_length=50, unique=True)
    transaction_type = models.IntegerField('Tipo de Categoria', choices=TransactionType.choices, default=TransactionType.ENTRADA )

    def __str__(self):
        return self.category
