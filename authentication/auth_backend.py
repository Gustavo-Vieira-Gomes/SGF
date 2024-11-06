from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from .models import UserCompany

class CompanyAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                # Verifica se o usuário está associado a uma empresa ativa
                user_company = UserCompany.objects.get(user=user)
                if user_company and user.is_active:
                    return user
        except User.DoesNotExist:
            return None
        except UserCompany.DoesNotExist:
            return None
        return None
