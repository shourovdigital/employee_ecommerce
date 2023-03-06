# Generated by Django 4.1.6 on 2023-03-06 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_banks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=100)),
                ('supplier_phone', models.CharField(max_length=14)),
                ('supplier_email', models.EmailField(max_length=50)),
                ('supplier_address', models.CharField(max_length=200)),
                ('supplier_contact_person', models.CharField(max_length=100)),
                ('supplier_contact_person_designation', models.CharField(max_length=50)),
                ('supplier_contact_person_phone', models.CharField(max_length=14)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'suppliers',
            },
        ),
    ]
