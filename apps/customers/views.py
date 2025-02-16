from apps.customers.models import Customer
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    fields = ['name', 'cpf', 'cnpj', 'address', 'phone']
    success_url = reverse_lazy('customers:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    context_object_name = 'customers'
    paginate_by = 20
    
    def get_queryset(self):
        qs = Customer.objects.filter(user=self.request.user)
        if query := self.request.GET.get('q'):
            qs = qs.filter(name__icontains=query)
        return qs


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    fields = ['name', 'cpf', 'cnpj', 'address', 'phone']
    success_url = reverse_lazy('customers:list')


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    success_url = reverse_lazy('customers:list')
