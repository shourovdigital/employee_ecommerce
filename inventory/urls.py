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

    path('area-add', views.area_add, name='area_add'),
    path('area-list', views.area_list, name='area_list'),
    path('area-edit/<int:id>', views.area_edit, name='area_edit'),
    path('area-delete/<int:id>', views.area_delete, name='area_delete'),

    path('division-add', views.division_add, name='division_add'),
    path('division-list', views.division_list, name='division_list'),
    path('division-edit/<int:id>', views.division_edit, name='division_edit'),
    path('division-delete/<int:id>',views.division_delete, name='division_delete'),

    path('district-add', views.district_add, name='district_add'),
    path('district-list', views.district_list, name='district_list'),

    path('thana-add', views.thana_add, name='thana_add'),
    path('thana-list', views.thana_list, name='thana_list'),
    path('thana-edit/<int:id>', views.thana_edit, name='thana_edit'),
    path('thana-delete/<int:id>', views.thana_delete, name='thana_delete'),
]