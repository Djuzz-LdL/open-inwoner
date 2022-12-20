# Generated by Django 3.2.15 on 2022-11-28 15:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pdc", "0042_auto_20220929_1726"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="product",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="pdc.product",
                verbose_name="Product",
            ),
        ),
    ]
