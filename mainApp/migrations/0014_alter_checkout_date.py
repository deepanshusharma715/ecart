# Generated by Django 4.1.7 on 2023-05-29 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainApp", "0013_alter_checkout_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="checkout",
            name="date",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
