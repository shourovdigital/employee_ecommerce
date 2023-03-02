# Generated by Django 4.1.6 on 2023-03-01 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_apps', '0007_productlog'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentActivityLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(max_length=50)),
                ('activity_timestamp', models.DateTimeField(auto_now_add=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_apps.department')),
            ],
            options={
                'db_table': 'department_activity_log',
            },
        ),
    ]