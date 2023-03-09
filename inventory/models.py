from django.db import models

# Create your models here.
class Customers(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField(max_length=50)
    customer_phone = models.CharField(max_length=14)
    customer_address = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'customers'

class ExpenseCategory(models.Model):
    expense_category = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'expense_categories'


class Banks(models.Model):
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100)
    branch_name = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'banks'


class Suppliers(models.Model):
    supplier_name = models.CharField(max_length=100)
    supplier_phone = models.CharField(max_length=14)
    supplier_email = models.EmailField(max_length=50)
    supplier_address = models.CharField(max_length=200)
    supplier_contact_person = models.CharField(max_length=100)
    supplier_contact_person_designation = models.CharField(max_length=50)
    supplier_contact_person_phone = models.CharField(max_length=14)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'suppliers'


class Area(models.Model):
    area = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'areas'



class Division(models.Model):
    division = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'divisions'

class District(models.Model):
    division_name = models.ForeignKey(Division, on_delete=models.CASCADE)
    district_name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'districts'

class Thana(models.Model):
    division_for_thana = models.ForeignKey(Division, on_delete=models.CASCADE)
    district_for_thana = models.ForeignKey(District, on_delete=models.CASCADE)
    thana_name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'thana'