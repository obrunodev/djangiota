from django.db import models


class CustomerManager(models.Manager):
    def get_customers(self, request):
        qs = self.get_queryset().filter(user=request.user)
        if query := request.GET.get('q'):
            qs = qs.filter(name__icontains=query)
        return qs
    