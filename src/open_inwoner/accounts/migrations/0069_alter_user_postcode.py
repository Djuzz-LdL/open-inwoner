# Generated by Django 3.2.20 on 2023-12-04 09:07

from django.db import migrations

import localflavor.nl.models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0068_relax_email_constraint_for_eherkenning"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="postcode",
            field=localflavor.nl.models.NLZipCodeField(
                blank=True, default="", max_length=7, verbose_name="Postcode"
            ),
        ),
    ]
