from django.shortcuts import render, redirect
from employee_apps.models import *
from . import models

# Create your views here.
def inventory_home(request):
    return render(request, 'inventory/index.html')

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
    customers = models.Customers.objects.all().order_by('-id')
    context = {
        'customers' : customers
    }
    return render(request, 'inventory/customer-list.html', context)