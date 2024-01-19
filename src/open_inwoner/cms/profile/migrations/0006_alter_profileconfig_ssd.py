# Generated by Django 3.2.23 on 2023-12-13 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profile", "0005_remove_profileconfig_selected_categories"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profileconfig",
            name="ssd",
            field=models.BooleanField(
                default=False,
                help_text="Designates whether the 'Mijn uitkeringen' section is rendered or not. Should only be enabled if a CMS app has been created and the corresponding CMS page has been published.",
                verbose_name="Mijn uitkeringen",
            ),
        ),
    ]
