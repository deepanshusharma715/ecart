# Generated by Django 4.1.7 on 2023-05-25 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mainApp", "0009_whislist"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Whislist",
            new_name="Wishlist",
        ),
    ]
