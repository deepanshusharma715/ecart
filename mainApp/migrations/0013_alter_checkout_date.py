# Generated by Django 4.1.7 on 2023-05-29 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainApp", "0012_checkoutproduct_qty_checkoutproduct_total"),
    ]

    operations = [
        migrations.AlterField(
            model_name="checkout",
            name="date",
            field=models.DateTimeField(),
        ),
    ]
