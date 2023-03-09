# Generated by Django 4.1.6 on 2023-03-07 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_district'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thana',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thana_name', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('district_for_thana', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.district')),
                ('division_for_thana', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.division')),
            ],
            options={
                'db_table': 'thana',
            },
        ),
    ]
