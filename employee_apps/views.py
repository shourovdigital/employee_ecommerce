from django.shortcuts import render, redirect
from . import models
from django.db.models import F

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Product, ProductLog
import xlwt
from django.http import HttpResponse

from django.shortcuts import render, redirect
# from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from io import BytesIO


# Create your views here.
def homepage(request):
    return render(request, 'index.html')

# Department
def department_add(request):
    if request.method == 'POST':
        department = request.POST.get('department')

        models.Department.objects.create(
            department = department
        )

        return redirect('/department-list')
    return render(request, 'department-add.html')

def department_edit(request, id):
    get_department = models.Department.objects.get( id=id )
    context = {
        'get_department' : get_department
    }
    if request.method == 'POST':
        department = request.POST.get('department')
        
        models.Department.objects.filter( id=id).update(
            department = department
        )
        models.DepartmentActivityLog.objects.create(
            department_id = id,
            updated_department_name = department
        )
        return redirect('/department-list')
    return render(request, 'department-edit.html', context)


def department_list(request):
    departments = models.Department.objects.filter( status = True ).order_by('-id')
    context = {
        'department' : departments
    }
    return render(request, 'department-list.html', context)

def department_delete(request, id):
    models.Department.objects.filter( id=id ).update(
        status = False
    )
    return redirect('/department-list')


# Employee

def employee_add(request):
    if request.method == 'GET':
        get_department = models.Department.objects.filter(status=True)
        context = {
            'get_department' : get_department
        }
    else:
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        present_address = request.POST.get('present_address')
        permanent_address = request.POST.get('permanent_address')
        dob = request.POST.get('dob')
        fathers_name = request.POST.get('fathers_name')
        mothers_name = request.POST.get('mothers_name')
        job_title = request.POST.get('job_title')
        department = request.POST.get('department')

        models.Employee.objects.create(
            full_name = full_name,
            phone = phone,
            email = email,
            present_address = present_address,
            permanent_address = permanent_address,
            dob = dob,
            fathers_name = fathers_name,
            mothers_name = mothers_name,
            job_title = job_title,
            department_id = department
        )
        return redirect('/employee-list')
    return render(request, 'employee-add.html', context)

def employee_edit(request, id):
    get_employee_info = models.Employee.objects.get( id=id )
    get_department = models.Department.objects.filter(status=True)
    context = {
        'get_employee_info' : get_employee_info,
        'get_department' : get_department
    }
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        present_address = request.POST.get('present_address')
        permanent_address = request.POST.get('permanent_address')
        dob = request.POST.get('dob')
        fathers_name = request.POST.get('fathers_name')
        mothers_name = request.POST.get('mothers_name')
        job_title = request.POST.get('job_title')
        department = request.POST.get('department')

        models.Employee.objects.filter( id=id ).update(
            full_name = full_name,
            phone = phone,
            email = email,
            present_address = present_address,
            permanent_address = permanent_address,
            dob = dob,
            fathers_name = fathers_name,
            mothers_name = mothers_name,
            job_title = job_title,
            department_id = department
        )
        return redirect('/employee-list')
    return render(request, 'employee-edit.html', context)

def employee_delete(request, id):
    models.Employee.objects.filter( id=id).update(
        status = False
    )

    # models.Employee.objects.filter( id=id).delete()
    return redirect('/employee-list')


def employee_details(request, id):
    get_emp_details = models.Employee.objects.get( id=id )
    context = {
        'get_emp_details' : get_emp_details
    }
    return render(request, 'employee-details.html', context)

def employee_list(request):
    employee_list = models.Employee.objects.filter(status=True).order_by('-id')
    context = {
        'employee_list' : employee_list
    }
    return render(request, 'employee-list.html', context)


# Category
def category_add(request):
    if request.method == 'POST':
        category_add = request.POST.get('category_name')

        models.Category.objects.create(
            category_name = category_add
        )
        return redirect('/category-list')
    return render(request, 'category-add.html')


def category_list(request):
    searchText = request.GET.get('search')
    if searchText:
        category = models.Category.objects.filter(category_name__icontains=searchText, status = True).order_by('-id')
    else:
        category = models.Category.objects.filter(status = True).order_by('-id')
    context = {
        'category' : category
    }
    return render(request, 'category-list.html', context)


def category_edit(request, id):
    get_category = models.Category.objects.get( id=id )
    context = {
        'get_category' : get_category
    }
    if request.method == 'POST':
        category = request.POST.get('category')
        
        models.Category.objects.filter( id=id ).update(
            category_name = category
        )
        models.CategoryActivityLog.objects.create(
            category_name_id = id,
            updated_category_name = category
        )
        return redirect('/category-list')
    return render(request, 'category-edit.html', context)

def category_delete(request, id):
    models.Category.objects.filter( id=id ).update(
        status = False
    )
    return redirect('/category-list')

# Brand
def brand_add(request):
    if request.method == 'POST':
        brand_name = request.POST.get('brand_name')

        models.Brand.objects.create(
            brand_name = brand_name
        )
        return redirect('/brand-list')
    return render(request, 'brand-add.html')


def brand_list(request):
    get_brands = models.Brand.objects.filter(status=True).order_by('-id')
    context = {
        'get_brands' : get_brands
    }
    return render(request, 'brand-list.html', context)

def brand_edit(request, id):
    get_brands = models.Brand.objects.get( id=id )
    context = {
        'get_brands' : get_brands
    }
    if request.method == 'POST':
        brand_name = request.POST.get('brand_name')

        models.Brand.objects.filter( id=id ).update(
            brand_name = brand_name
        )
        models.BrandActivityLog.objects.create(
            brand_name_id = id,
            updated_brand_name = brand_name
        )
        return redirect('/brand-list')
    return render(request, 'brand-e dit.html', context)

def brand_delete(request, id):
    models.Brand.objects.filter( id=id ).update(
        status = False
    )
    return redirect('/brand-list')


# Size
def size_add(request):
    if request.method == 'POST':
        size_add = request.POST.get('size_name')

        models.Size.objects.create(
            size_name = size_add
        )
        return redirect('/size-list')

    return render(request, 'size-add.html')


def size_list(request):
    get_size = models.Size.objects.filter( status=True )
    context = {
        'get_size' : get_size
    }
    return render(request, 'size-list.html', context)

def size_edit(request, id):
    get_sizes = models.Size.objects.get( id=id )
    context = {
        'get_sizes' : get_sizes
    }
    if request.method == 'POST':
        size_name = request.POST.get('size_name')

        models.Size.objects.filter( id=id ).update(
            size_name = size_name
        )
        models.SizeActivityLog.objects.create(
            size_name_id = id,
            updated_size_name = size_name
        )
        return redirect('/size-list')
    return render(request, 'size-edit.html', context)

def size_delete(request, id):
    models.Size.objects.filter( id=id ).update(
        status = False
    )
    return redirect('/size-delete')

# Color 
def color_add(request):
    if request.method == 'POST':
        color_name = request.POST.get('color_name')

        models.Color.objects.create(
            color_name = color_name
        )
        return redirect('/color-list')
    return render(request, 'color-add.html')

def color_list(request):
    get_colors = models.Color.objects.filter( status = True ).order_by('-id')
    context = {
        'get_colors' : get_colors
    }
    return render(request, 'color-list.html', context)

def color_edit(request, id):
    get_colors = models.Color.objects.get( id=id )
    context = {
        'get_colors' : get_colors
    }
    if request.method == 'POST':
        color_name = request.POST.get('color_name')

        models.Color.objects.filter( id=id ).update(
            color_name = color_name
        )
        models.ColorActivityLog.objects.create(
            color_name_id = id,
            updated_color_name = color_name
        )
        return redirect('/color-list')
    return render(request, 'color-edit.html', context)

def color_delete(request, id):
    models.Color.objects.filter( id=id ).update(
        status = False
    )
    return redirect('/color-list')


# Unit 
def unit_add(request):
    if request.method == 'POST':
        unit_name = request.POST.get('unit_name')

        models.Unit.objects.create(
            unit_name = unit_name
        )
        return redirect('/unit-list')
    return render(request, 'unit-add.html')

def unit_list(request):
    get_units = models.Unit.objects.filter(status=True).order_by('-id')
    context = {
        'get_units' : get_units
    }
    return render(request, 'unit-list.html', context)

def unit_edit(request, id):
    get_unit = models.Unit.objects.get( id=id )
    context = {
        'get_unit' : get_unit
    }
    if request.method == 'POST':
        unit_name = request.POST.get('unit_name')

        models.Unit.objects.filter( id=id ).update(
            unit_name = unit_name
        )
        models.UnitActivityLog.objects.create(
            unit_id = id,
            updated_unit_name = unit_name
        )
        return redirect('/unit-list')
    return render(request, 'unit-edit.html', context)

def unit_delete(request, id):
    models.Unit.objects.filter( id=id ).update(
        status = False
    )
    return redirect('/unit-list')


# Product Add
def product_add(request):
    if request.method == 'GET':
        get_category = models.Category.objects.filter(status=True)
        get_color = models.Color.objects.filter(status=True)
        get_size = models.Size.objects.filter(status=True)
        get_brand = models.Brand.objects.filter(status=True)
        get_unit = models.Unit.objects.filter(status=True)

        context = {
            'get_category' : get_category,
            'get_color' : get_color,
            'get_size' : get_size,
            'get_brand' : get_brand,
            'get_unit' : get_unit
        }
        return render(request, 'product-add.html', context)
        
    else:
        product_name = request.POST.get('product_name')
        regular_price = request.POST.get('regular_price')
        sales_price = request.POST.get('sales_price')
        category = request.POST.get('category')
        color = request.POST.get('color')
        size = request.POST.get('size')
        brand = request.POST.get('brand')
        unit = request.POST.get('unit')
        details = request.POST.get('details')
        stock_qty = request.POST.get('stock_qty')

        models.Product.objects.create(
            product_name = product_name,
            regular_price = regular_price,
            sales_price = sales_price,
            category_id = category,
            color_id = color,
            size_id = size,
            brand_id = brand,
            unit_id = unit,
            details = details,
            stock_qty = stock_qty
        )
        return redirect('/product-list')

def product_list(request):
    get_products = models.Product.objects.filter(status=True).order_by('-id')
    context = {
        'get_products' : get_products
    }
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        stock_qty = request.POST.get('stock_qty')

        models.Product.objects.filter(id=product_id).update(
            stock_qty = F('stock_qty') + stock_qty
        )
        models.QtyUpdateLog.objects.create(
            updated_qty = stock_qty,
            product_name_id = product_id
        )

        return redirect('/product-list')

    return render(request, 'product-list.html', context)

# def product_edit(request, id):
    get_product_info = models.Product.objects.get( id=id )
    get_category = models.Category.objects.filter( status=True )
    get_color = models.Color.objects.filter( status=True )
    get_size = models.Size.objects.filter( status=True )
    get_brand = models.Brand.objects.filter( status=True )
    get_unit = models.Unit.objects.filter( status=True )
    context = {
        'get_product_info' : get_product_info,
        'get_category' : get_category,
        'get_color' : get_color,
        'get_size' : get_size,
        'get_brand' : get_brand,
        'get_unit' : get_unit
    }
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        regular_price = request.POST.get('regular_price')
        sales_price = request.POST.get('sales_price')
        category = request.POST.get('category')
        color = request.POST.get('color')
        size = request.POST.get('size')
        brand = request.POST.get('brand')
        unit = request.POST.get('unit')
        details = request.POST.get('details')
        stock_qty = request.POST.get('stock_qty')

        models.Product.objects.filter(id=id).update(
            product_name = product_name,
            regular_price = regular_price,
            sales_price = sales_price,
            category_id = category,
            color_id = color,
            size_id = size,
            brand_id = brand,
            unit_id = unit,
            details = details,
            stock_qty = stock_qty
        )
        return redirect('/product-list')
    return render(request, 'product-edit.html', context)

def product_edit(request, id):
    get_product_info = models.Product.objects.get(id=id)
    get_category = models.Category.objects.filter(status=True)
    get_color = models.Color.objects.filter(status=True)
    get_size = models.Size.objects.filter(status=True)
    get_brand = models.Brand.objects.filter(status=True)
    get_unit = models.Unit.objects.filter(status=True)
    context = {
        'get_product_info' : get_product_info,
        'get_category' : get_category,
        'get_color' : get_color,
        'get_size' : get_size,
        'get_brand' : get_brand,
        'get_unit' : get_unit
    }
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        regular_price = request.POST.get('regular_price')
        sales_price = request.POST.get('sales_price')
        category = request.POST.get('category')
        color = request.POST.get('color')
        size = request.POST.get('size')
        brand = request.POST.get('brand')
        unit = request.POST.get('unit')
        stock_qty = request.POST.get('stock_qty')
        details = request.POST.get('details')

        models.Product.objects.filter(id=id).update(
            product_name = product_name,
            regular_price = regular_price,
            sales_price = sales_price,
            category_id = category,
            color_id = color,
            size_id = size,
            brand_id = brand,
            unit_id = unit,
            stock_qty = stock_qty,
            details = details

        )
        return redirect('/product-list')
    return render(request, 'product-edit.html', context)

def product_details(request):
    
    return render(request, 'product-details.html')


# Helpfrom akkas vi
# def product_edit(request, id):
    if request.method == "GET":
        get_product_info = models.Product.objects.get(id=id)
        get_category = models.Category.objects.filter(status=True)
        get_color = models.Color.objects.filter(status=True)
        get_size = models.Size.objects.filter(status=True)
        get_brand = models.Brand.objects.filter(status=True)
        get_unit = models.Unit.objects.filter(status=True)
        context = {
            'get_product_info' : get_product_info,
            'get_category' : get_category,
            'get_color' : get_color,
            'get_size' : get_size,
            'get_brand' : get_brand,
            'get_unit' : get_unit
        }
        
        return render(request, 'product-edit.html', context)
    
    else:
        product_name = request.POST.get('product_name')
        regular_price = request.POST.get('regular_price')
        sales_price = request.POST.get('sales_price')
        category = int(request.POST.get('category'))
        color = int(request.POST.get('color'))
        size = int(request.POST.get('size'))
        brand = int(request.POST.get('brand'))
        unit = int(request.POST.get('unit'))
        stock_qty = request.POST.get('stock_qty')
        details = request.POST.get('details')

        models.Product.objects.filter(id=id).update(
            product_name = product_name,
            regular_price = regular_price,
            sales_price = sales_price,
            category_id = category,
            color_id = color,
            size_id = size,
            brand_id = brand,
            unit_id = unit,
            stock_qty = stock_qty,
            details = details

        )
        return redirect('/product-list')

def product_details(request, id):
    get_details = models.Product.objects.get(id=id)
    context = {
        'get_details' :get_details
    }
    return render(request, 'product-details.html', context)

def product_delete(request, id):
    models.Product.objects.filter(id=id).update(
        status = False
    )
    return redirect('/product-list')

def product_sales_price_update(request, id):
    get_sales_price = models.Product.objects.get(id=id)
    context = {
        'get_sales_price' : get_sales_price
    }
    if request.method == 'POST':
        sales_price = request.POST.get('product_sales_price_update')

        models.Product.objects.filter(id=id).update(
            sales_price = sales_price
        )
        models.SalesPriceUpdateLog.objects.create(
            updated_sales_price = sales_price,
            product_name_id = id

        )
        return redirect('/product-list')
    return render(request, 'product-sales-price-update.html', context)

def product_regular_price_update(request, id):
    get_regular_price = models.Product.objects.get(id=id)
    context = {
        'get_regular_price' : get_regular_price
    }
    if request.method == 'POST':
        regular_price = request.POST.get('product_regular_price_update')
        
        models.Product.objects.filter(id=id).update(
            regular_price = regular_price
        )
        models.RegularPriceUpdateLog.objects.create(
            product_name_id = id,
            updated_regular_price = regular_price
        )
        
        return redirect('/product-list')
    return render(request, 'product-regular-price-update.html', context)

# ----------------------------------------------

@receiver(post_save, sender=Product)
def log_product_save(sender, instance, created, **kwargs):
    action = 'created' if created else 'updated'
    ProductLog.objects.create(action=action, product=instance)

@receiver(post_delete, sender=Product)
def log_product_delete(sender, instance, **kwargs):
    ProductLog.objects.create(action='deleted', product=instance)


def product_log(request, id):
    product_instance = Product.objects.get(id=id)
    logs = ProductLog.objects.filter(product=product_instance)
    context = {'product': product_instance, 'logs': logs}
    return render(request, 'product-log.html', context)




# Product Info Excel Export
def product_excel_export(request): 
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="products.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Sheet1') # this will make a sheet named Users Data

    head_style = xlwt.easyxf('pattern: pattern solid, fore_colour green; font: bold on; align: horiz center')
    product_name_style = xlwt.easyxf('align: horiz left; borders: left thin, right thin, top thin, bottom thin;')
    regular_price_style = xlwt.easyxf('align: horiz left; borders: left thin, right thin, top thin, bottom thin;')
    sales_price_style = xlwt.easyxf('align: horiz left; borders: left thin, right thin, top thin, bottom thin;')
    stock_style = xlwt.easyxf('align: horiz left; borders: left thin, right thin, top thin, bottom thin;')
    category_style = xlwt.easyxf('align: horiz left; borders: left thin, right thin, top thin, bottom thin;')
    color_style = xlwt.easyxf('align: horiz left; borders: left thin, right thin, top thin, bottom thin;')
    size_style = xlwt.easyxf('align: horiz left; borders: left thin, right thin, top thin, bottom thin;')
    brand_style = xlwt.easyxf('align: horiz left; borders: left thin, right thin, top thin, bottom thin;')
    unit_style = xlwt.easyxf('align: horiz left; borders: left thin, right thin, top thin, bottom thin;')
    details_style = xlwt.easyxf('align: horiz left; borders: left thin, right thin, top thin, bottom thin;')
    column_style = [product_name_style, regular_price_style, sales_price_style, stock_style, category_style, color_style, size_style, brand_style, unit_style, details_style]

    col_widths = [1000*10, 5000, 10000, 15000, 15000, 3000, 8000, 8000, 3000, 5000]
    for col_num, col_width in enumerate(col_widths):
        ws.col(col_num).width = col_width
    
    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Product Name', 'Regular Price', 'Sales Price', 'Stock Quantity', 'Category Name', 'Color', 'Size', 'Brand', 'Unit', 'Details']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], style = head_style ) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = models.Product.objects.filter(status=True).values_list('product_name', 'regular_price', 'sales_price', 'stock_qty', 'category__category_name', 'color__color_name', 'size__size_name', 'brand__brand_name', 'unit__unit_name', 'details')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], style=column_style[col_num])

    wb.save(response)

    return response


# Employee Info Excel Export
def employee_info_excel_export(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="employee.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Sheet1') # this will make a sheet named Users Data

    head_style = xlwt.easyxf('pattern: pattern solid, fore_colour green; font: bold on; align: horiz center')
    full_name_style = xlwt.easyxf('font: bold on; align: horiz left; borders: left thin, right thin, top thin, bottom thin;')
    phone_number_style = xlwt.easyxf('font: bold on; align: horiz left; borders: left thin, right thin, top thin, bottom thin;')
    email_style = xlwt.easyxf('borders: left thin, right thin, top thin, bottom thin; align: horiz left; borders: left thin, right thin, top thin, bottom thin;')
    present_address_style = xlwt.easyxf('font: bold on; align: horiz left;borders: left thin, right thin, top thin, bottom thin;')
    permanent_address_style = xlwt.easyxf('font: bold on; align: horiz left;borders: left thin, right thin, top thin, bottom thin;')
    dob_style = xlwt.easyxf('pattern: pattern solid, fore_colour yellow; font: bold on; align: horiz left;borders: left thin, right thin, top thin, bottom thin;')
    fname_style = xlwt.easyxf('font: bold on; align: horiz left;borders: left thin, right thin, top thin, bottom thin;')
    mname_style = xlwt.easyxf('font: bold on; align: horiz left;borders: left thin, right thin, top thin, bottom thin;')
    job_title_style = xlwt.easyxf('font: bold on; align: horiz left;borders: left thin, right thin, top thin, bottom thin;')
    department_style = xlwt.easyxf('pattern: pattern solid, fore_colour green;font: bold on; align: horiz left;borders: left thin, right thin, top thin, bottom thin;')
    columns_styles = [full_name_style, phone_number_style, email_style, present_address_style, permanent_address_style, dob_style, fname_style, mname_style, job_title_style, department_style ]

    col_widths = [1000*10, 5000, 10000, 15000, 15000, 3000, 8000, 8000, 3000, 5000]
    for col_num, col_width in enumerate(col_widths):
        ws.col(col_num).width = col_width

    
    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Full Name', 'Phone Number', 'Email Address', 'Present Address', 'Permanent Address', 'Date Of Birth', "Father's Name", "Mother's Name", 'Job Title', 'Department' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], style=head_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = models.Employee.objects.all().values_list('full_name', 'phone', 'email', 'present_address', 'permanent_address', 'dob', 'fathers_name', 'mothers_name', 'job_title', 'department__department')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            if col_num ==5:
                ws.write(row_num, col_num, row[col_num].strftime('%Y-%m-%d') , style=columns_styles[col_num])
            else:
                ws.write(row_num, col_num, row[col_num], style=columns_styles[col_num])
            
           

    wb.save(response)

    return response

# Unit List Excel Export
def unit_list_excel_export(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="units.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Sheet1') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Unit Name' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = models.Unit.objects.all().values_list('unit_name')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response

# Size List Excel Export
def size_list_excel_export(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="sizes.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Sheet1') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Size Name' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = models.Size.objects.all().values_list('size_name')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response

# Department List Excel Export
def department_list_excel_export(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="department.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Sheet1') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Department Name' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = models.Department.objects.all().values_list('department')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response

# Color List Excel Export
def color_list_excel_export(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="colors.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Sheet1') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Color Name' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = models.Color.objects.all().values_list('color_name')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response

# Color List Excel Export
def color_list_excel_export(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="colors.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Sheet1') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Color Name' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = models.Color.objects.all().values_list('color_name')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response

# Category List Excel Export
def category_list_excel_export(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="categories.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Sheet1') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    reversed = 'pattern: pattern solid, fore_color blue; font: color white;'

    columns = ['category Name' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = models.Category.objects.all().values_list('category_name')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style, reversed)

    wb.save(response)

    return response

# Brand List Excel Export
def brand_list_excel_export(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="brand.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Sheet1') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    font_style.font.italic = True
    
    
    columns = ['Brand Name' ]
    

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = models.Brand.objects.all().values_list('brand_name')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    
    

    wb.save(response)

    return response


# Unit export as pdf
def export_units_to_pdf(request):
    # Get all units from the database
    units = models.Unit.objects.all()

    # Create a file-like buffer to receive PDF data.
    buffer = BytesIO()

    # Create the PDF object, using the buffer as its "file."
    doc = SimpleDocTemplate(buffer, pagesize=A4)

    # Create a table and populate it with data from the queryset
    data = []
    data.append(['ID', 'Unit Name'])
    for unit in units:
        data.append([unit.id, unit.unit_name])
    t = Table(data)

    # Define the table style
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
    ])

    # Apply the table style to the table
    t.setStyle(style)

    # Add the table to the PDF document
    elements = []
    elements.append(t)
    doc.build(elements)

    # File response with PDF content.
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="units.pdf"'

    return response
 