# Generated by Django 3.2.20 on 2023-10-16 07:57

from django.db import migrations, models
import django.db.models.deletion
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ("openzaak", "0024_zaaktypeconfig_contact_subject_code"),
    ]

    operations = [
        migrations.CreateModel(
            name="ZaakTypeStatusTypeConfig",
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
                    "statustype_url",
                    models.URLField(max_length=1000, verbose_name="Statustype URL"),
                ),
                (
                    "omschrijving",
                    models.CharField(max_length=80, verbose_name="Omschrijving"),
                ),
                (
                    "statustekst",
                    models.CharField(max_length=1000, verbose_name="Statustekst"),
                ),
                (
                    "zaaktype_uuids",
                    django_better_admin_arrayfield.models.fields.ArrayField(
                        base_field=models.UUIDField(verbose_name="Zaaktype UUID"),
                        default=list,
                        size=None,
                    ),
                ),
                (
                    "status_indicator",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("info", "Info"),
                            ("warning", "Warning"),
                            ("failure", "Failure"),
                            ("success", "Success"),
                        ],
                        help_text="Determines what will be shown to the user if a case is set to this status",
                        max_length=32,
                        verbose_name="Statustype indicator",
                    ),
                ),
                (
                    "status_indicator_text",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text="Determines the text that will be shown to the user if a case is set to this status",
                        verbose_name="Statustype indicator",
                    ),
                ),
                (
                    "zaaktype_config",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="openzaak.zaaktypeconfig",
                    ),
                ),
            ],
            options={
                "verbose_name": "Zaaktype Statustype Configuration",
            },
        ),
        migrations.AddConstraint(
            model_name="zaaktypestatustypeconfig",
            constraint=models.UniqueConstraint(
                fields=("zaaktype_config", "statustype_url"),
                name="unique_zaaktype_config_statustype_url",
            ),
        ),
    ]
