# Generated by Django 4.1.7 on 2023-05-20 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainApp", "0004_buyer"),
    ]

    operations = [
        migrations.AddField(
            model_name="buyer",
            name="username",
            field=models.CharField(default="", max_length=30),
        ),
    ]
