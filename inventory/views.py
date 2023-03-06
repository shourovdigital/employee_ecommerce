from django.shortcuts import render
from employee_apps.models import *

# Create your views here.
def inventory_home(request):
    return render(request, 'inventory/index.html')