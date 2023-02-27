# Generated by Django 3.2.15 on 2023-02-20 16:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pdc", "0050_alter_product_summary"),
    ]

    # https://docs.djangoproject.com/en/3.2/howto/writing-migrations/#changing-a-manytomanyfield-to-use-a-through-model

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.RunSQL(
                    sql="ALTER TABLE pdc_product_categories RENAME TO pdc_categoryproduct",
                    reverse_sql="ALTER TABLE pdc_categoryproduct RENAME TO pdc_product_categories",
                ),
            ],
            state_operations=[
                migrations.CreateModel(
                    name="CategoryProduct",
                    fields=[
                        (
                            "id",
                            models.AutoField(
                                auto_created=True,
                                primary_key=True,
                                serialize=False,
                                verbose_name="ID",
                            ),
                        ),
                        (
                            "category",
                            models.ForeignKey(
                                on_delete=django.db.models.deletion.CASCADE,
                                to="pdc.category",
                            ),
                        ),
                        (
                            "product",
                            models.ForeignKey(
                                on_delete=django.db.models.deletion.CASCADE,
                                to="pdc.product",
                            ),
                        ),
                    ],
                ),
                migrations.AlterField(
                    model_name="product",
                    name="categories",
                    field=models.ManyToManyField(
                        help_text="Categories which the product relates to",
                        related_name="products",
                        through="pdc.CategoryProduct",
                        to="pdc.Category",
                        verbose_name="Categories",
                    ),
                ),
            ],
        )
    ]
