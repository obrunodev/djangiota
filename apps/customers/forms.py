from apps.customers.models import Customer
from shared.forms import BaseModelForm


class CustomerForm(BaseModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'cpf', 'cnpj', 'address', 'phone']
