from django.db import models


# Create your models here.
class Department(models.Model):
    department = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'department_db'

from django.db import models


class DepartmentActivityLog(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    updated_department_name = models.CharField(max_length=50)
    updated_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'department_activity_log'




class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)
    email = models.CharField(max_length=50)
    present_address = models.CharField(max_length=300)
    permanent_address = models.CharField(max_length=300)
    dob = models.DateField(auto_now_add=False, null=True, blank=True)
    fathers_name = models.CharField(max_length=100)
    mothers_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'employee_db'

# Unit
class Unit(models.Model):
    unit_name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'unit_tbl'

class UnitActivityLog(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    updated_unit_name = models.CharField(max_length=50)
    updated_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'unit_activity_log'


# Category
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'category_tbl'

class CategoryActivityLog(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    updated_category_name = models.CharField(max_length=50)
    updated_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'category_activity_log'


# Color
class Color(models.Model):
    color_name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'color_tbl'

class ColorActivityLog(models.Model):
    color_name = models.ForeignKey(Color, on_delete=models.CASCADE)
    updated_color_name = models.CharField(max_length=50)
    updated_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'color_activity_log'

# Size
class Size(models.Model):
    size_name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'size_tbl'

class SizeActivityLog(models.Model):
    size_name = models.ForeignKey(Size, on_delete=models.CASCADE)
    updated_size_name = models.CharField(max_length=50)
    updated_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'size_activity_log'  

# Brand
class Brand(models.Model):
    brand_name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'brand_tbl'

class BrandActivityLog(models.Model):
    brand_name = models.ForeignKey(Brand, on_delete=models.CASCADE)
    updated_brand_name = models.CharField(max_length=50)
    updated_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'brand_activity_log'

# Product
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    regular_price = models.CharField(max_length=30)
    sales_price = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True, blank=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    details = models.TextField()
    stock_qty = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'product_tbl'



# Log
class ProductLog(models.Model):
    ACTION_CHOICES = (
        ('created', 'Created'),
        ('updated', 'Updated'),
        ('deleted', 'Deleted'),
    )

    action = models.CharField(choices=ACTION_CHOICES, max_length=10)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'activity_tbl'


class QtyUpdateLog(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    update_time = models.DateTimeField(auto_now_add=True)
    updated_qty = models.CharField(max_length=30)

    class Meta:
        db_table = 'qty_update_log'

class SalesPriceUpdateLog(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    updated_sales_price = models.CharField(max_length=30)
    update_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'sales_price_update_log'

class RegularPriceUpdateLog(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    updated_regular_price = models.CharField(max_length=30)
    updated_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'regular_price_update_log'



class EduDepartments(models.Model):
    department_name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'edu_departments'