# Generated by Django 3.2.20 on 2023-10-06 08:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("objects", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="objectslist",
            name="bsn_path",
            field=models.CharField(
                blank=True,
                help_text="The path to the bsn value from data, for example: 'identificatie.value'",
                max_length=250,
                verbose_name="BSN Path",
            ),
        ),
        migrations.AddField(
            model_name="objectslist",
            name="component",
            field=models.CharField(
                choices=[("link", "Link"), ("map", "Map")],
                default="link",
                max_length=30,
                verbose_name="Component",
            ),
        ),
        migrations.AddField(
            model_name="objectslist",
            name="date_order",
            field=models.CharField(
                choices=[("+", "Ascend"), ("-", "Descent")],
                default="-",
                help_text="Order date on acending or decending.",
                max_length=1,
                verbose_name="Date Order",
            ),
        ),
        migrations.AddField(
            model_name="objectslist",
            name="map_lat",
            field=models.DecimalField(
                decimal_places=6,
                default=52.1326,
                max_digits=9,
                verbose_name="Map starting Latitude",
            ),
        ),
        migrations.AddField(
            model_name="objectslist",
            name="map_long",
            field=models.DecimalField(
                decimal_places=6,
                default=5.2913,
                max_digits=9,
                verbose_name="Map starting Longitude",
            ),
        ),
        migrations.AddField(
            model_name="objectslist",
            name="map_zoom_level",
            field=models.IntegerField(
                default=3,
                validators=[
                    django.core.validators.MaxValueValidator(18),
                    django.core.validators.MinValueValidator(1),
                ],
                verbose_name="Map starting Longitude",
            ),
        ),
        migrations.AddField(
            model_name="objectslist",
            name="no_results_message",
            field=models.TextField(
                default="no results found",
                help_text="Text message to tell the user that there are no results found",
                verbose_name="No results message",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="objectslist",
            name="object_date",
            field=models.CharField(
                default="start_at",
                help_text="The path to the date, for example: 'start_at'",
                max_length=250,
                verbose_name="Object Date",
            ),
        ),
        migrations.AddField(
            model_name="objectslist",
            name="object_link",
            field=models.CharField(
                default="data.formulier.value",
                help_text="The path to the url, for example: 'data.formulier.value'",
                max_length=250,
                verbose_name="Object Link",
            ),
        ),
        migrations.AddField(
            model_name="objectslist",
            name="object_title",
            field=models.CharField(
                default="data.title",
                help_text="The path to the title, for example: 'data.title'",
                max_length=250,
                verbose_name="Object Title",
            ),
        ),
        migrations.AddField(
            model_name="objectslist",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("open", "Open"),
                    ("ingediend", "Submitted"),
                    ("verwerkt", "Processed"),
                    ("gesloten", "Closed"),
                ],
                max_length=250,
                verbose_name="Status",
            ),
        ),
    ]
