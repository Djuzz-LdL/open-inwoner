# Generated by Django 3.2.15 on 2023-06-01 08:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("extensions", "0003_commonextension_menu_icon"),
    ]

    operations = [
        migrations.AlterField(
            model_name="commonextension",
            name="menu_icon",
            field=models.CharField(
                blank=True,
                choices=[
                    ("person", "Home"),
                    ("description", "Products"),
                    ("inbox", "Inbox"),
                    ("inventory_2", "Cases"),
                    ("group", "Collaborate"),
                    ("help_outline", "Help"),
                ],
                help_text="Icon in het menu",
                max_length=32,
                verbose_name="Icon",
            ),
        ),
    ]
