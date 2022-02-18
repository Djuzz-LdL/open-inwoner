# Generated by Django 3.2.12 on 2022-02-14 14:38

from django.db import migrations, models
import django.utils.timezone
import localflavor.nl.models


class Migration(migrations.Migration):

    dependencies = [
        ("pdc", "0022_question"),
        ("accounts", "0027_auto_20220214_1440"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="birthday",
            field=models.DateField(blank=True, null=True, verbose_name="Birthday"),
        ),
        migrations.AlterField(
            model_name="user",
            name="bsn",
            field=localflavor.nl.models.NLBSNField(
                blank=True, max_length=12, null=True, verbose_name="Bsn"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="city",
            field=models.CharField(
                blank=True, default="", max_length=250, verbose_name="City"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="date_joined",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Date joined"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                max_length=254, unique=True, verbose_name="Email address"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(
                blank=True, default="", max_length=255, verbose_name="First name"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="housenumber",
            field=models.CharField(
                blank=True, default="", max_length=250, verbose_name="House number"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(
                default=True,
                help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                verbose_name="Active",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_prepopulated",
            field=models.BooleanField(
                default=False,
                help_text="Indicates if fields have been prepopulated by Haal Central API.",
                verbose_name="Prepopulated",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(
                default=False,
                help_text="Designates whether the user can log into this admin site.",
                verbose_name="Staff status",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(
                blank=True, default="", max_length=255, verbose_name="Last name"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="login_type",
            field=models.CharField(
                choices=[
                    ("default", "Email en Wachtwoord"),
                    ("digid", "DigiD"),
                    ("eherkenning", "eHerkenning"),
                ],
                default="default",
                max_length=250,
                verbose_name="Login type",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="postcode",
            field=localflavor.nl.models.NLZipCodeField(
                blank=True, max_length=7, null=True, verbose_name="Postcode"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="rsin",
            field=models.CharField(
                blank=True, max_length=9, null=True, verbose_name="Rsin"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="selected_themes",
            field=models.ManyToManyField(
                blank=True,
                related_name="selected_by",
                to="pdc.Category",
                verbose_name="Selected themes",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="street",
            field=models.CharField(
                blank=True, default="", max_length=250, verbose_name="Street"
            ),
        ),
    ]
