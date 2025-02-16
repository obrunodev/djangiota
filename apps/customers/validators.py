import re
from django.core.exceptions import ValidationError

def validate_cpf(value):
    if not re.match(r'^\d{11}$', value):
        raise ValidationError('O CPF deve conter 11 dígitos numéricos.')

def validate_cnpj(value):
    if value and not re.match(r'^\d{14}$', value):
        raise ValidationError('O CNPJ deve conter 14 dígitos numéricos.')

def validate_phone(value):
    if not re.match(r'^\d{11}$', value):
        raise ValidationError('O telefone deve conter 11 dígitos numéricos.')
