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
    path('expense-category-list', views.expense_category_list, name='expense_category_list'),
    path('expense-category-edit/<int:id>', views.expense_category_edit, name='expense_category_edit'),
    path('expense-category-delete/<int:id>', views.expense_category_delete, name='expense_category_delete'),
    path('bank-add', views.bank_add, name='bank_add'),
    path('bank-list', views.bank_list, name='bank_list'),
    path('bank-edit/<int:id>', views.bank_edit, name='bank_edit'),
    path('bank-delete/<int:id>', views.bank_delete, name='bank_delete'),
    path('supplier-add', views.supplier_add, name='supplier_add'),
    path('supplier-list', views.supplier_list, name='supplier_list'),
    path('supplier-edit/<int:id>', views.supplier_edit, name='supplier_edit'),
    path('supplier-delete/<int:id>', views.supplier_delete, name='supplier_delete'),
    path('supplier-details/<int:id>', views.supplier_details, name='supplier_details'),
        
]