# Generated by Django 4.2.16 on 2025-01-07 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("openklant", "0015_openklant2config"),
    ]

    operations = [
        migrations.CreateModel(
            name="KlantenSysteemConfig",
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
                    "primary_backend",
                    models.CharField(
                        choices=[("esuite", "ESUITE"), ("openklant2", "OPENKLANT2")],
                        max_length=10,
                        help_text="Choose the primary backend for retrieving klanten data. Changes to klanten data will be saved to both backends (if configured).",
                    ),
                ),
            ],
            options={
                "verbose_name": "Configuratie Klanten Systeem",
            },
        ),
    ]
