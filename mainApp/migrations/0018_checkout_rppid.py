# Generated by Django 4.1.7 on 2023-06-06 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainApp", "0017_buyer_otp"),
    ]

    operations = [
        migrations.AddField(
            model_name="checkout",
            name="rppid",
            field=models.CharField(default="", max_length=30),
        ),
    ]
