from django.shortcuts import render, redirect
from employee_apps.models import *
from . import models

# Create your views here.
def inventory_home(request):
    return render(request, 'inventory/index.html')


# Customer 
def customer_add(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        customer_phone = request.POST.get('customer_phone')
        customer_email = request.POST.get('customer_email')
        customer_address = request.POST.get('customer_address')

        models.Customers.objects.create(
            customer_name = customer_name,
            customer_phone = customer_phone,
            customer_email = customer_email,
            customer_address = customer_address
        )
        return redirect('/inv/customer-list')
    return render(request, 'inventory/customer-add.html')


def customer_list(request):
    customers = models.Customers.objects.filter(deleted=False).order_by('-id')
    context = {
        'customers' : customers
    }
    return render(request, 'inventory/customer-list.html', context)


def customer_edit(request, id):
    if request.method == 'GET':
        get_customers = models.Customers.objects.get(id=id)
        context = {
            'get_customers' : get_customers
        }
        return render(request, 'inventory/customer-edit.html', context)
    
    else:
        customer_name = request.POST['customer_name']
        customer_phone = request.POST['customer_phone']
        customer_email = request.POST['customer_email']
        customer_address = request.POST['customer_address']
    
    # or
    #     customer_name = request.POST.get('customer_name')
    #     customer_phone = request.POST.get('customer_phone')
    #     customer_email = request.POST.get('customer_email')
    #     customer_address = request.POST.get('customer_address')


        models.Customers.objects.filter(id=id).update(
            customer_name = customer_name,
            customer_phone = customer_phone,
            customer_email = customer_email,
            customer_address = customer_address
        )
        return redirect('/inv/customer-list')
    

def customer_delete(request, id):
    models.Customers.objects.filter(id=id).update(
        deleted = True
    )
    return redirect('/inv/customer-list')


def customer_details(request, id):
    customer_details = models.Customers.objects.get(id=id)
    context = {
        'customer_details' : customer_details
    }
    return render(request, 'inventory/customer-details.html', context)


# Expense
def expense_category_add(request):
    if request.method == 'POST':
        expense_category = request.POST.get('expense_category')

        models.ExpenseCategory.objects.create(
            expense_category = expense_category
        )
        return redirect('/inv/expense-category-list')
    return render(request, 'inventory/expense-category-add.html')

def expense_category_list(request):
    expense_category = models.ExpenseCategory.objects.filter(deleted=False).order_by('-id')
    context = {
        'excat' : expense_category
    }
    return render(request, 'inventory/expense-category-list.html', context)


def expense_category_edit(request, id):
    if request.method == 'GET':
        expense_categories = models.ExpenseCategory.objects.get(id=id)
        context = {
            'expense_categories' : expense_categories
        }
        return render(request, 'inventory/expense-category-edit.html', context)
    else:
        expense_category = request.POST.get('expense_category')

        models.ExpenseCategory.objects.filter(id=id).update(
            expense_category = expense_category
        )
        return redirect('/inv/expense-category-list')
    

def expense_category_delete(request, id):
    models.ExpenseCategory.objects.filter(id=id).update(
        deleted = True
    )
    return redirect('/inv/expense-category-list')


# Bank
def bank_add(request):
    if request.method == 'POST':
        bank_name = request.POST.get('bank_name')
        account_number = request.POST.get('account_number')
        branch_name = request.POST.get('branch_name')

        models.Banks.objects.create(
            bank_name = bank_name,
            account_number = account_number,
            branch_name = branch_name
        )
        return redirect('/inv/bank-list')
    return render(request, 'inventory/bank-add.html')

def bank_list(request):
    banks = models.Banks.objects.filter(deleted=False).order_by('-id')
    context = {
        'banks' : banks
    }
    return render(request, 'inventory/bank-list.html', context)


def bank_edit(request, id):
    if request.method == 'GET':
        banks = models.Banks.objects.get(id=id)
        context = {
            'banks' : banks
        }
        return render(request, 'inventory/bank-edit.html', context)
    else:
        bank_name = request.POST['bank_name']
        account_number = request.POST['account_number']
        branch_name = request.POST['branch_name']

        models.Banks.objects.filter(id=id).update(
            bank_name = bank_name,
            account_number = account_number,
            branch_name = branch_name
        )
        return redirect('/inv/bank-list')
    
def bank_delete(request, id):
    models.Banks.objects.filter(id=id).update(
        deleted = True
    )
    return redirect('/inv/bank-list')


# Supplier
def supplier_add(request):
    if request.method == 'POST':
        supplier_name = request.POST.get('supplier_name')
        supplier_phone = request.POST.get('supplier_phone')
        supplier_email = request.POST.get('supplier_email')
        supplier_address = request.POST.get('supplier_address')
        supplier_contact_person = request.POST.get('supplier_contact_person')
        supplier_contact_person_designation = request.POST.get('supplier_contact_person_designation')
        supplier_contact_person_phone = request.POST.get('supplier_contact_person_phone')

        models.Suppliers.objects.create(
            supplier_name = supplier_name,
            supplier_phone = supplier_phone,
            supplier_email = supplier_email,
            supplier_address = supplier_address,
            supplier_contact_person = supplier_contact_person,
            supplier_contact_person_designation = supplier_contact_person_designation,
            supplier_contact_person_phone = supplier_contact_person_phone
        )
        return redirect('/inv/supplier-list')
    return render(request, 'inventory/supplier-add.html')

def supplier_list(request):
    suppliers = models.Suppliers.objects.all().order_by('-id')
    context = {
        'suppliers' : suppliers
    }
    return render(request, 'inventory/supplier-list.html', context)