# Generated by Django 5.0.1 on 2024-02-28 19:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0006_alter_orderitems_order_alter_product_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="mobile",
            field=models.CharField(max_length=20),
        ),
    ]