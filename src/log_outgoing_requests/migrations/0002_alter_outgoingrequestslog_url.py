# Generated by Django 3.2.15 on 2023-03-20 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("log_outgoing_requests", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="outgoingrequestslog",
            name="url",
            field=models.URLField(
                blank=True,
                default="",
                help_text="The url of the outgoing request.",
                max_length=1000,
                verbose_name="URL",
            ),
        ),
    ]
