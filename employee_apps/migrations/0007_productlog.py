# Generated by Django 4.1.6 on 2023-03-01 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_apps', '0006_product_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('created', 'Created'), ('updated', 'Updated'), ('deleted', 'Deleted')], max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_apps.product')),
            ],
            options={
                'db_table': 'activity_tbl',
            },
        ),
    ]
