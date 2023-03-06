from django.db import models

# Create your models here.
class Customers(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField(max_length=50)
    customer_phone = models.CharField(max_length=14)
    customer_address = models.TextField()

    class Meta:
        db_table = 'customers'