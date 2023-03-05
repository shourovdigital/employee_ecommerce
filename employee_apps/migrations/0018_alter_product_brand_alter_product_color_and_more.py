# Generated by Django 4.1.6 on 2023-03-05 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_apps', '0017_sizeactivitylog_coloractivitylog_categoryactivitylog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee_apps.brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee_apps.color'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee_apps.size'),
        ),
    ]
