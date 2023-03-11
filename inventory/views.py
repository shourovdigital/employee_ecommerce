from django.shortcuts import render, redirect
from employee_apps.models import *
from . import models
from django.http import JsonResponse
# Create your views here.
def inventory_home(request):
    return render(request, 'inventory/index.html')


# Customer 
def customer_add(request):
    if request.method == 'GET':
        get_division = models.Division.objects.all()
        get_district = models.District.objects.all()
        get_thana = models.Thana.objects.all()
        context = {
            'get_division' : get_division,
            'get_district' : get_district,
            'get_thana' : get_thana
        }
        return render(request, 'inventory/customer-add.html', context)

    else:
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


def customer_list(request):
    customers = models.Customers.objects.filter(deleted=False).order_by('-id')
    context = {
        'customers' : customers
    }
    return render(request, 'inventory/customer-list.html', context)


def customer_edit(request, id):
    if request.method == 'GET':
        get_customers = models.Customers.objects.get(id=id)
        get_division = models.Division.objects.all()
        get_district = models.District.objects.all()
        get_thana = models.Thana.objects.all()
        context = {
            'get_customers' : get_customers,
            'get_division' : get_division,
            'get_district' : get_district,
            'get_thana' : get_thana
        }
        return render(request, 'inventory/customer-edit.html', context)
    
    else:
        customer_name = request.POST['customer_name']
        customer_phone = request.POST['customer_phone']
        customer_email = request.POST['customer_email']
        division = request.POST['division']
        district = request.POST['district']
        thana = request.POST['thana']
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
            division_id = division,
            district_id = district,
            thana_id = thana,
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
    suppliers = models.Suppliers.objects.filter(deleted=False).order_by('-id')
    context = {
        'suppliers' : suppliers
    }
    return render(request, 'inventory/supplier-list.html', context)

def supplier_edit(request, id):
    if request.method == 'GET':
        suppliers = models.Suppliers.objects.get(id=id)
        context = {
            'suppliers' : suppliers
        }
        return render(request, 'inventory/supplier-edit.html', context)
    else:
        supplier_name = request.POST['supplier_name']
        supplier_phone = request.POST['supplier_phone']
        supplier_email = request.POST['supplier_email']
        supplier_address = request.POST['supplier_address']
        supplier_contact_person = request.POST['supplier_contact_person']
        supplier_contact_person_designation = request.POST['supplier_contact_person_designation']
        supplier_contact_person_phone = request.POST['supplier_contact_person_phone']

        models.Suppliers.objects.filter(id=id).update(
            supplier_name = supplier_name,
            supplier_phone = supplier_phone,
            supplier_email = supplier_email,
            supplier_address = supplier_address,
            supplier_contact_person = supplier_contact_person,
            supplier_contact_person_designation = supplier_contact_person_designation,
            supplier_contact_person_phone = supplier_contact_person_phone
        )
        return redirect('/inv/supplier-list')
    
def supplier_delete(request, id):
    models.Suppliers.objects.filter(id=id).update(
        deleted = True
    )
    return redirect('/inv/supplier-list')


def supplier_details(request, id):
    supplier_details = models.Suppliers.objects.get(id=id)
    context = {
        'details' : supplier_details
    }
    return render(request, 'inventory/supplier-details.html', context)

# Area
def area_add(request):
    if request.method == 'POST':
        area = request.POST.get('area')

        models.Area.objects.create(
            area = area
        )
        return redirect('/inv/area-list')
    return render(request, 'inventory/area-add.html')


def area_list(request):
    areas = models.Area.objects.filter(deleted=False).order_by('-id')
    context = {
        'areas' : areas
    }
    return render(request, 'inventory/area-list.html', context)

def area_edit(request, id):
    if request.method == 'GET':
        areas = models.Area.objects.get(id=id)
        context = {
            'areas' : areas
        }
        return render(request, 'inventory/area-edit.html', context)
    else:
        area = request.POST.get('area')

        models.Area.objects.filter(id=id).update(
            area = area
        )
        return redirect('/inv/area-list')
    
def area_delete(request, id):
    models.Area.objects.filter(id=id).update(
        deleted = True
    )
    return redirect('/inv/area-list')


# Division
def division_add(request):
    if request.method == 'POST':
        division = request.POST['division']

        models.Division.objects.create(
            division = division
        )
        return redirect('/inv/division-list')
    return render(request, 'inventory/division-add.html')


def division_list(request):
    divisions = models.Division.objects.filter(deleted=False).order_by('-id')
    context = {
        'divisions' : divisions
    }
    return render(request, 'inventory/division-list.html', context)


def division_edit(request, id):
    if request.method == 'GET':
        get_division = models.Division.objects.get(id=id)
        context = {
            'division_name' : get_division.division
        }
        return render(request, 'inventory/division-edit.html', context)
    else:
        division = request.POST['division']

        models.Division.objects.filter(id=id).update(
            division = division
        )
        return redirect('/inv/division-list')
    

def division_delete(request, id):
    models.Division.objects.filter(id=id).update(
        deleted = True
    )
    return redirect('/inv/division-list')

# District
def district_add(request):
    if request.method == 'GET':
        get_divisions = models.Division.objects.all()
        context = {
            'get_divisions' : get_divisions
        }
        return render(request, 'inventory/district-add.html', context)
    else:
        division = request.POST.get('division_name')
        district_name = request.POST.get('district_name')

        models.District.objects.create(
            division_name_id = division,
            district_name = district_name
        )
        return redirect('/inv/district-list')

def district_list(request):
    districts = models.District.objects.filter(deleted=False).order_by('-id')
    context = {
        'districts' : districts
    }
    return render(request, 'inventory/district-list.html', context)


def district_edit(request, id):
    if request.method == 'GET':
        district_info = models.District.objects.get(id=id)
        get_division = models.Division.objects.all()
        context = {
            'district_info' : district_info,
            'get_division' : get_division
        }
        return render(request, 'inventory/district-edit.html', context)
    else:
        division_name = request.POST.get('division_name')
        district_name = request.POST.get('district_name')

        models.District.objects.filter(id=id).update(
            division_name_id = division_name,
            district_name = district_name
        )
        return redirect('/inv/district-list')
    
def district_delete(request, id):
    models.District.objects.filter(id=id).update(
        deleted = True
    )
    return redirect('/inv/district-list')

# Thana
def thana_add(request):
    if request.method == 'GET':
        get_division = models.Division.objects.all()
        get_district = models.District.objects.all()
        context = {
            'get_division' : get_division,
            'get_district' : get_district
        }
        return render(request, 'inventory/thana-add.html', context)
    else:
        division_for_thana = request.POST.get('division_for_thana')
        district_for_thana = request.POST.get('district_for_thana')
        thana_name = request.POST.get('thana_name')

        models.Thana.objects.create(
            division_for_thana_id = division_for_thana,
            district_for_thana_id = district_for_thana,
            thana_name = thana_name
        )
        return redirect('/inv/thana-list')



def thana_list(request):
    get_thana = models.Thana.objects.filter(deleted=False).order_by('-id')
    context = {
        'get_thana' : get_thana
    }
    return render(request, 'inventory/thana-list.html', context)


def thana_edit(request, id):
    if request.method == 'GET':
        get_thana = models.Thana.objects.get(id=id)
        get_district = models.District.objects.all()
        get_division = models.Division.objects.all()
        context = {
            'get_thana' : get_thana,
            'get_district' : get_district,
            'get_division' : get_division
        }
        return render(request, 'inventory/thana-edit.html', context)
    else:
        division_for_thana = request.POST.get('division_for_thana')
        district_for_thana = request.POST.get('district_for_thana')
        thana_name = request.POST.get('thana_name')

        models.Thana.objects.filter(id=id).update(
            division_for_thana_id = division_for_thana,
            district_for_thana_id = district_for_thana,
            thana_name = thana_name
        )
        return redirect('/inv/thana-list')
    
def thana_delete(request, id):
    models.Thana.objects.filter(id=id).update(
        deleted = True
    )
    return redirect('/inv/thana-list')







def load_division(request):
    division = models.Division.objects.all()
    return JsonResponse(list(division.values('id','division')),safe=False)

def load_district(request):
    division_id = request.GET.get('division_id')
    district = models.District.objects.filter(division_name=division_id)
    return JsonResponse(list(district.values('id','district_name')),safe=False)


def load_thana(request):
    division_id = request.GET.get('division_id')
    district_id = request.GET.get('district_id')
    district = models.Thana.objects.filter(division_for_thana = division_id,district_for_thana=district_id)
    return JsonResponse(list(district.values('id','thana_name')),safe=False)