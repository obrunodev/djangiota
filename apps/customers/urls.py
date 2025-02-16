from django.urls import path
from apps.customers import views

app_name = 'customers'
urlpatterns = [
    path('', views.CustomerListView.as_view(), name='list'),
    path('create/', views.CustomerCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.CustomerUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.CustomerDeleteView.as_view(), name='delete'),
]