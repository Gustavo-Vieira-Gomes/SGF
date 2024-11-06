from django.db import models
from companies.models import Company
from django.contrib.auth.models import User


class UserCompany(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.company.name}'