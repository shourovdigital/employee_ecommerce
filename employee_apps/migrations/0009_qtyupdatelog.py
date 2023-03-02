# Generated by Django 4.1.6 on 2023-03-01 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_apps', '0008_departmentactivitylog'),
    ]

    operations = [
        migrations.CreateModel(
            name='QtyUpdateLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('updated_qty', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'qty_update_log',
            },
        ),
    ]
