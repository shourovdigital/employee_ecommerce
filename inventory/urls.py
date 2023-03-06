from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_home, name='inventory_home'),
    path('customer-add', views.customer_add, name='customer_add'),
    path('customer-list', views.customer_list, name='customer_list'),
    path('customer-edit/<int:id>', views.customer_edit, name='customer_edit'),
    path('customer-delete/<int:id>', views.customer_delete, name='customer_delete'),
    path('customer-details/<int:id>', views.customer_details, name='customer_details'),
    path('expense-category-add', views.expense_category_add, name='expense_category_add'),
    
]