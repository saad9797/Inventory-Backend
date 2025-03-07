# Generated by Django 5.1.1 on 2025-03-07 06:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmodel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mrf',
            old_name='dept_id',
            new_name='DepartmentID',
        ),
        migrations.RenameField(
            model_name='mrf',
            old_name='mrf_id',
            new_name='MrfID',
        ),
        migrations.RemoveField(
            model_name='product',
            name='UnitPrice',
        ),
        migrations.RemoveField(
            model_name='purchaseorder',
            name='OrderDate',
        ),
        migrations.RemoveField(
            model_name='purchaseorder',
            name='Stand',
        ),
        migrations.AddField(
            model_name='mrf',
            name='Purpose',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='mrf',
            name='Reference',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='mrf',
            name='quantity_recieved',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='mrf',
            name='recieved_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='MajorHead',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='Specification',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='DateRecieved',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='DeliveryChalanNumber',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.AlterField(
            model_name='category',
            name='CategoryName',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.AlterField(
            model_name='category',
            name='Description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='department_name',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.AlterField(
            model_name='department',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='Quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='WarehouseLocation',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.AlterField(
            model_name='mrf',
            name='quantity_requested',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='mrf',
            name='request_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='mrf',
            name='status',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='Description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='ProductName',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='TotalAmount',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorderdetails',
            name='CostPrice',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorderdetails',
            name='Quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorderdetails',
            name='Subtotal',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='Address',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='Contact',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='SupplierName',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserID', models.AutoField(primary_key=True, serialize=False)),
                ('Email', models.EmailField(max_length=254, null=True)),
                ('Role', models.CharField(default='Unknown', max_length=255)),
                ('Password', models.CharField(default='Unknown', max_length=255)),
                ('DepartmentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pmodel.department')),
            ],
        ),
    ]
