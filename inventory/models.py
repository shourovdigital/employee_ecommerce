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


