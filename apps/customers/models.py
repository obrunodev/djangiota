from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db import models
from shared.models import BaseModel
from apps.customers.managers import CustomerManager


class Customer(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(_('Nome'), max_length=255)
    cpf = models.CharField(_('CPF'), max_length=11)
    cnpj = models.CharField(_('CNPJ'), max_length=14, blank=True, null=True)
    address = models.CharField(_('Endereço'), max_length=255)
    phone = models.CharField(_('Telefone'), max_length=11)
    
    objects = CustomerManager()
    
    class Meta:
        ordering = ['name']
        verbose_name = _('Cliente')
        verbose_name_plural = _('Clientes')

    def __str__(self):
        return self.name
