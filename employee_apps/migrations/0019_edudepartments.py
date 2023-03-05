# Generated by Django 4.1.6 on 2023-03-05 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_apps', '0018_alter_product_brand_alter_product_color_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EduDepartments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'edu_departments',
            },
        ),
    ]
