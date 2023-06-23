# Generated by Django 4.1.7 on 2023-05-26 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mainApp", "0010_rename_whislist_wishlist"),
    ]

    operations = [
        migrations.CreateModel(
            name="Checkout",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "paymentMode",
                    models.IntegerField(
                        choices=[(1, "COD"), (1, "Net Banking")], default=1
                    ),
                ),
                (
                    "paymentStatus",
                    models.IntegerField(
                        choices=[(1, "Pending"), (2, "Done")], default=1
                    ),
                ),
                (
                    "orderStatus",
                    models.IntegerField(
                        choices=[
                            (1, "Order Placed"),
                            (2, "Ready to Dispatch"),
                            (3, "Dispatched"),
                            (4, "Out of Delivery"),
                            (5, "Delivered"),
                        ],
                        default=1,
                    ),
                ),
                ("subtotal", models.IntegerField()),
                ("shipping", models.IntegerField()),
                ("final", models.IntegerField()),
                ("date", models.DateTimeField(auto_now=True)),
                (
                    "buyer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="mainApp.buyer"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CheckoutProduct",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "checkout",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mainApp.checkout",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mainApp.product",
                    ),
                ),
            ],
        ),
    ]
