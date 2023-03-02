from django.urls import path
from . import views

urlpatterns =[
    path('', views.homepage, name='homepage'),
    path('employee-add', views.employee_add, name='employee_add'),
    path('employee-list', views.employee_list, name='employee_list'),
    path('employee-details/<int:id>', views.employee_details, name='employee_details'),
    path('employee-edit/<int:id>', views.employee_edit, name='employee_edit'),
    path('employee-delete/<int:id>', views.employee_delete, name='employee_delete'),
    path('employee-info-excel-export', views.employee_info_excel_export, name='employee_info_excel_export'), #for excel export
    path('department-add', views.department_add, name='department_add'),
    path('department-edit/<int:id>', views.department_edit, name='department_edit'),
    path('department-list', views.department_list, name='department_list'),
    path('department-delete/<int:id>', views.department_delete, name='department_delete'),
    path('department-list-excel-export', views.department_list_excel_export, name='department_list_excel_export'), # Excel
    path('category-add', views.category_add, name='category_add'),
    path('category-list', views.category_list, name='category_list'),
    path('category-edit/<int:id>', views.category_edit, name='category_edit'),
    path('category-delete/<int:id>', views.category_delete, name='category_delete'),
    path('category-list-excel-export', views.category_list_excel_export, name='category_list_excel_export'),
    path('brand-add', views.brand_add, name='brand_add'),
    path('brand-list', views.brand_list, name='brand_list'),
    path('brand-edit/<int:id>', views.brand_edit, name='brand_edit'),
    path('brand-delete/<int:id>', views.brand_delete, name='brand_delete'),
    path('brand-list-excel-export', views.brand_list_excel_export, name='brand_list_excel_export'), #Excel Export
    path('size-add', views.size_add, name='size_add'),
    path('size-list', views.size_list, name='size_list'),
    path('size-edit/<int:id>', views.size_edit, name='size_edit'),
    path('size-delete/<int:id>', views.size_delete, name='size_delete'),
    path('size-list-excel-export', views.size_list_excel_export, name='size_list_excel_export'), #For Excel Export
    path('color-add', views.color_add, name='color_add'),
    path('color-list', views.color_list, name='color_list'),
    path('color-edit/<int:id>', views.color_edit, name='color_edit'),
    path('color-delete/<int:id>', views.color_delete, name='color_delete'),
    path('color-list-excel-export', views.color_list_excel_export, name='color_list_excel_export'), #For Excel Export
    path('unit-add', views.unit_add, name='unit_add'),
    path('unit-list', views.unit_list, name='unit_list'),
    path('unit-edit/<int:id>', views.unit_edit, name='unit_edit'),
    path('unit-delete/<int:id>', views.unit_delete, name='unit_delete'),
    path('unit-list-excel-export', views.unit_list_excel_export, name='unit_list_excel_export'), #for Excel Export
    path('product-add', views.product_add, name='product_add'),
    path('product-list', views.product_list, name='product_list'),
    path('product-details/<int:id>', views.product_details, name='product_details'),
    path('product-edit/<int:id>', views.product_edit, name='product_edit'),
    path('product-delete/<int:id>', views.product_delete, name='product_delete'),
    path('product-sales-price-update/<int:id>/', views.product_sales_price_update, name='product_sales_price_update'),
    path('product-regular-price-update/<int:id>', views.product_regular_price_update, name='product_regular_price_update'),
    path('product-log/<int:id>', views.product_log, name='product_log'),
    path('product-excel-export', views.product_excel_export, name='product_excel_export')

]