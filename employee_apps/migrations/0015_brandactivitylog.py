# Generated by Django 4.1.6 on 2023-03-02 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_apps', '0014_rename_department_name_departmentactivitylog_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandActivityLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_brand_name', models.CharField(max_length=50)),
                ('updated_time', models.DateTimeField(auto_now_add=True)),
                ('brand_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_apps.brand')),
            ],
            options={
                'db_table': 'brand_activity_log',
            },
        ),
    ]
