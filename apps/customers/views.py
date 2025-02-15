from apps.customers.models import Customer
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
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
