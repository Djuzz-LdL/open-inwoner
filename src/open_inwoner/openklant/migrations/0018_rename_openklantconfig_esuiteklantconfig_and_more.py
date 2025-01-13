# Generated by Django 4.2.16 on 2025-01-09 10:52

from django.db import migrations, models

import open_inwoner.openklant.models


class Migration(migrations.Migration):

    dependencies = [
        ("zgw_consumers", "0022_set_default_service_slug"),
        ("openklant", "0017_alter_openklant2config_service"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="OpenKlantConfig",
            new_name="ESuiteKlantConfig",
        ),
        migrations.AlterField(
            model_name="klantensysteemconfig",
            name="primary_backend",
            field=models.CharField(
                choices=[("esuite", "ESUITE"), ("openklant2", "OPENKLANT2")],
                help_text="Choose the primary backend for retrieving klanten data. Changes to klanten data will be saved to both backends (if configured).",
                max_length=10,
                validators=[open_inwoner.openklant.models.validate_primary_backend],
            ),
        ),
        migrations.AlterModelOptions(
            name="esuiteklantconfig",
            options={"verbose_name": "eSuite Klant configuration"},
        ),
    ]
