# Generated by Django 4.2.4 on 2023-08-13 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_no',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='invoicedetail',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='invoicedetail',
            name='unit_price',
            field=models.IntegerField(),
        ),
    ]
